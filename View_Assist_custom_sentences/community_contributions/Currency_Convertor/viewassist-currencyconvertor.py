import requests, re

#
# https://pyyaml.org/wiki/PyYAMLDocumentation
#
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

#
# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#pyscript-executor
#
@pyscript_executor
def read_yaml(filename=None, key=None):
    try:
        yaml = load(open(filename, 'r'), Loader=Loader)[key]
        return yaml, None
    except Exception as exc:
        return None, exc

#
# https://www.geeksforgeeks.org/python-similarity-metrics-of-strings/
# 
from difflib import SequenceMatcher

def currency2code(currency=None, filename=None):
    currencies, exc = read_yaml(filename, 'currencies')
    if exc:
        return None, None, exc
    
    maxdiff = 0
    code = None
    for key, value in currencies.items():
        diff = SequenceMatcher(None, currency.lower(), key.lower()).ratio()
        if diff == 1:
            return value, diff, None
        else:
            if diff > maxdiff:
                maxdiff = diff
                code = value
    return code, maxdiff, None

def text2digit(text=None, lang=None, filename=None):
    digits, exc = read_yaml(filename, lang)
    if exc:
        return None, None, exc
    
    digit = [value for key, value in digits.items() if text.lower() in key.lower()]
    return digit, None

@service(supports_response="optional")
def currencyconvertor(rapidapikey=None, currencyfrom=None, currencyto=None):
    """yaml
    name: View Assist Currency Convertor
    description: Request currency to be convertor from one to another
    fields:
        rapidapikey:
            description: Your Rapi Api Key from https://rapidapi.com/pwshub-pwshub-default/api/crypto-market-prices
            example: Enter Your Rapid API Key Here
            required: true
            selector:
                text:
        currencyfrom:
            description: What currency to convert from
            example: us dollar
            required: true
            selector:
                text:
        currencyto:
            description: What currency to convert from
            example: euro
            required: true
            selector:
                text:
    """ 

    # localization: use prefered language from hass object
    currencyfile = "/config/custom_sentences/"+ hass.config.language + "/viewassist-currencyconvertor.currencies.yaml"
    digitfile = "/config/pyscript/viewassist-currencyconvertor.digits.yaml"
    
    # if currencyfrom is None, then intend is "exchange" and get preferred currency from hass object
    if not currencyfrom:
        codefrom = hass.config.currency
        amount = 1
    else:
        try:
            # codefrom contains amount as text or numbers
            amount, currency = currencyfrom.split(" ", 1)
            if not amount.isdigit():
                digits, exception = text2digit(amount, hass.config.language, digitfile)
                if exception:
                    errno, strerror = exception.args
                    response_variable = {"error": errno, "message": strerror, "data": { "filepath": digitfile }}
                    return response_variable
                amount = digits[0]

            codefrom, similarity, exception = currency2code(currency, currencyfile)
            # log.info(similarity)
            if exception:
                errno, strerror = exception.args
                response_variable = {"error": errno, "message": strerror, "data": { "filepath": currencyfile }}
                return response_variable
        except ValueError:
            codefrom = None

    codeto, similarity, exception = currency2code(currencyto, currencyfile)
    # log.info(similarity)
    
    if exception:
        errno, strerror = exception.args
        response_variable = {"error": errno, "message": strerror, "data": { "filepath": currencyfile }}
        return response_variable

    if not codefrom or not codeto:
        response_variable = {"error": -1, "message": "Unknown currency", "data": { "currency from": currencyfrom, "currency to": currencyto }}
        return response_variable

    url = "https://crypto-market-prices.p.rapidapi.com/currencies/convert?from="+ codefrom + "&to=" + codeto + "&amount=" + str(amount)
    headers = {
        'x-rapidapi-key': rapidapikey,
        'x-rapidapi-host': "crypto-market-prices.p.rapidapi.com"
    }

    r = task.executor(requests.get, url, headers=headers)
    
    if r.status_code == requests.codes.ok:
        response_variable = r.json()
    else:
        response_variable = {"error": r.status_code, "message": "Error request", "data": r.json()}
    return response_variable
