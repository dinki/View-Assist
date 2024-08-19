import requests,re

# Based on
# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#pyscript-executor
# https://pyyaml.org/wiki/PyYAMLDocumentation

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

@pyscript_executor
def currencyToCode(currencyfrom=None, currencyto=None, filename=None):
    try:
        with open(filename, 'r') as fd:
            currencies = load(fd, Loader=Loader)['currencies']
            codefrom = [value for key, value in currencies.items() if currencyfrom.lower() in key.lower()]
            codeto = [value for key, value in currencies.items() if currencyto.lower() in key.lower()]
        return codefrom, codeto, None
    except Exception as exc:
        return None, None, exc

@pyscript_executor
def replaceTextWithNumerals(currencyfrom=None, numerals_fp=None):
    try:
        with open(filename,'r') as fd:
            numerals = load(fd, Loader=Loader)['numerals']
            numeral = (value for key, value in numerals.items() if currencyfrom.lower() in key.lower())

        return currencyfrom, None
    except Exception as exc:
        return None, None, exc

@service(supports_response="optional")
def currency_convertor(currencyfrom=None, currencyto=None, amount=None, rapidapikey=None, language=None, return_response=True):
    """yaml
    name: View Assist Currency Convertor
    description: Request currency to be convertor from one to another
    fields:
        currencyfrom:
            description: What currency to convert from
            example: us dollar
            required: true
            selector:
                text:
        currencyto:
            description: What currency to convert to
            example: euro
            required: true
            selector:
                text:
        amount:
            description: How much do you want to convert
            example: 100
            required: false
            selector:
                text:
        rapidapikey:
            description: Your Rapi Api Key from https://rapidapi.com/pwshub-pwshub-default/api/crypto-market-prices
            example: Enter Your Rapid API Key Here
            required: true
            selector:
                text:
        language:
            description: The language you want to use for currency names
            example: en
            required: true
            selector:
                text:
    """ 

    # if amount is None then fromcurrency contains amount and currency name
    if not amount:
        amount, currencyfrom = currencyfrom.split(' ', 1)
        if amount.isdigit():
            amount = int(amount)
        else:
            numerals_fp ="/config/pyscript/" + language + "/numerals.yaml"
            amount, currencyfrom = replaceTextWithNumerals(currencyfrom, numerals_fp).split(' ', 1)

    currency_fp = "/config/pyscript/"+ language +"/currencies.yaml"
    codefrom, codeto, exception = currencyToCode(currencyfrom, currencyto, currency_fp)

    if exception:
        errno, strerror = exception.args
        response_variable = {"error": errno, "message": strerror, "data": { "filepath": currency_fp }}
        return response_variable

    if not codefrom or not codeto:
        response_variable = {"error": -1, "message": "Unknown currency", "data": { "currency from": currencyfrom, "currency to": currencyto }}
        return response_variable

    # if amount is none:
    #   amount = 1
    url = "https://crypto-market-prices.p.rapidapi.com/currencies/convert?from="+ codefrom[0] + "&to=" + codeto[0] + "&amount=" + amount    
    headers = {
        'x-rapidapi-key': rapidapikey,
        'x-rapidapi-host': "crypto-market-prices.p.rapidapi.com"
    }

    r = task.executor(requests.get, url, headers=headers)
    
    if r.status_code == requests.codes.ok:
        response_variable = r.json()
    else:
        response_variable = {"error": r.status_code, "data": r.json()}
    return response_variable
