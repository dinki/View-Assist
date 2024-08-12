import requests,re
@service(supports_response="optional")
def currency_convertor(currencyfrom=None, currencyto=None, amount=None, return_response=True):
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
            description: What currency to convert from
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
    """ 
    # You must get a Rapid API Key (free) to use this script
    # Get your free key for crypto-market-prices by following this link:
    # https://rapidapi.com/pwshub-pwshub-default/api/crypto-market-prices
    # Then, enter that value in the variable below:
    rapidapikey = "Enter Your Rapid API Key Here"

    currencies = {
    "albanian leks": "ALL",
    "algerian dinars": "DZD",
    "angolan kwanzas": "AOA",
    "argentine pesos": "ARS",
    "armenian drams": "AMD",
    "australian dollars": "AUD",
    "azerbaijani manats": "AZN",
    "bahamian dollars": "BSD",
    "bahraini dinars": "BHD",
    "bangladeshi takas": "BDT",
    "barbados dollars": "BBD",
    "belarusian rubles": "BYN",
    "belize dollars": "BZD",
    "bermudian dollars": "BMD",
    "bolivian bolivianos": "BOB",
    "bosnia and herzegovina markas": "BAM",
    "botswana pulas": "BWP",
    "brazilian reals": "BRL",
    "british pounds": "GBP",
    "brunei dollars": "BND",
    "bulgarian levs": "BGN",
    "burundi francs": "BIF",
    "cambodian riels": "KHR",
    "canadian dollars": "CAD",
    "cape verde escudos": "CVE",
    "cayman islands dollars": "KYD",
    "cfa beac francs": "XAF",
    "cfa bceao francs": "XOF",
    "cfp francs": "XPF",
    "chilean pesos": "CLP",
    "chinese yuan renminbis": "CNY",
    "colombian pesos": "COP",
    "costa rican colons": "CRC",
    "croatian kunas": "HRK",
    "cuban pesos": "CUP",
    "czech korunas": "CZK",
    "danish krones": "DKK",
    "djibouti francs": "DJF",
    "dominican pesos": "DOP",
    "east caribbean dollars": "XCD",
    "egyptian pounds": "EGP",
    "ethiopian birrs": "ETB",
    "euros": "EUR",
    "fiji dollars": "FJD",
    "gambian dalasis": "GMD",
    "georgian laris": "GEL",
    "ghanaian cedis": "GHS",
    "guatemalan quetzals": "GTQ",
    "guinea francs": "GNF",
    "haitian gourdes": "HTG",
    "honduran lempiras": "HNL",
    "hong kong dollars": "HKD",
    "hungarian forints": "HUF",
    "iceland kronas": "ISK",
    "indian rupees": "INR",
    "indonesian rupiahs": "IDR",
    "iranian rials": "IRR",
    "iraqi dinars": "IQD",
    "israeli new shekels": "ILS",
    "jamaican dollars": "JMD",
    "japanese yens": "JPY",
    "jordanian dinars": "JOD",
    "kazakhstan tenges": "KZT",
    "kenyan shillings": "KES",
    "korean wons": "KRW",
    "kuwaiti dinars": "KWD",
    "kyrgyzstani soms": "KGS",
    "lao kips": "LAK",
    "lebanese pounds": "LBP",
    "lesotho lotis": "LSL",
    "libyan dinars": "LYD",
    "macau patacas": "MOP",
    "macedonia denars": "MKD",
    "malawi kwachas": "MWK",
    "malaysian ringgits": "MYR",
    "mauritius rupees": "MUR",
    "mexican pesos": "MXN",
    "moldovan leus": "MDL",
    "moroccan dirhams": "MAD",
    "myanmar kyats": "MMK",
    "namibian dollars": "NAD",
    "nepalese rupees": "NPR",
    "netherlands antillian guilders": "ANG",
    "new zealand dollars": "NZD",
    "nicaraguan cordoba oros": "NIO",
    "nigerian nairas": "NGN",
    "norwegian krones": "NOK",
    "omani rials": "OMR",
    "pakistan rupees": "PKR",
    "panamanian balboas": "PAB",
    "paraguay guaranis": "PYG",
    "peruvian sols": "PEN",
    "philippine pesos": "PHP",
    "polish zlotys": "PLN",
    "qatari rials": "QAR",
    "romanian leus": "RON",
    "russian rubles": "RUB",
    "rwanda francs": "RWF",
    "saudi riyals": "SAR",
    "serbian dinars": "RSD",
    "seychelles rupees": "SCR",
    "singapore dollars": "SGD",
    "somali shillings": "SOS",
    "south african rands": "ZAR",
    "sri lanka rupees": "LKR",
    "sudanese pounds": "SDG",
    "swaziland lilangenis": "SZL",
    "swedish kronas": "SEK",
    "swiss francs": "CHF",
    "syrian pounds": "SYP",
    "taiwan dollars": "TWD",
    "tanzanian shillings": "TZS",
    "thai bahts": "THB",
    "trinidad and tobago dollars": "TTD",
    "tunisian dinars": "TND",
    "turkish liras": "TRY",
    "turkmenistan manats": "TMT",
    "ugandan shillings": "UGX",
    "ukraine hryvnias": "UAH",
    "united arab emirates dirhams": "AED",
    "uruguay pesos": "UYU",
    "u.s. dollars": "USD",
    "uzbekistan soms": "UZS",
    "venezuelan bolivars": "VES",
    "vietnamese dongs": "VND",
    "yemeni rials": "YER",
    "zambian kwachas": "ZMW"
    }

    fromvalue = [value for key, value in currencies.items() if currencyfrom.lower() in key.lower()]
    tovalue = [value for key, value in currencies.items() if currencyto.lower() in key.lower()]
    # if amount is none:
    #   amount = 1
    headers = {
        'x-rapidapi-key': rapidapikey,
        'x-rapidapi-host': "crypto-market-prices.p.rapidapi.com"
    }    
    url = "https://crypto-market-prices.p.rapidapi.com/currencies/convert?from="+ fromvalue[0] + "&to=" + tovalue[0] + "&amount=" + amount    
    headers = {
        'x-rapidapi-key': "5c7a1d645amsh8a7166fbd666088p1b67dbjsn7ff924890195",
        'x-rapidapi-host': "crypto-market-prices.p.rapidapi.com"
    }

    r = task.executor(requests.get, url, headers=headers)
  
    if r.status_code == requests.codes.ok:
        response_variable = r.json()
        #log.warning(str(fromvalue))
        log.warning(amount)
        return response_variable
    else:
        response_variable = {"error": r.status_code, "data": r.json()}
