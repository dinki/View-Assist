# https://pyyaml.org/wiki/PyYAMLDocumentation

import os
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

#
# https://hacs-pyscript.readthedocs.io/en/stable/reference.html#pyscript-executor
#
@pyscript_executor
def read_response(intent=None, response=None, filename=None):
        
    try:
        sentence = load(open(filename, 'r'), Loader=Loader)['responses']['intents'][intent][response]
        return sentence, None
    except Exception as exc:
        return None, exc

@service(supports_response="optional")
def response_handler(intent=None, response=None, custom=None, **kwargs):
    """yaml
    name: View Assist Response Handler
    description: Create a response message from localized response sentences and named values
    fields:
        intent:
            description: The intent from response sentence
            example: ConvertCurrency
            required: true
            selector:
                text:
        response:
            description: Which response sentence from intent should be used
            example: speech
            required: true
            selector:
                text:
        custom:
            description: Which viewassist custom automation should be used
            example: viewassist_currencyconvertor
            required: true
            selector:
                text:
        kwargs:
            description: Named values to be replaced in the response sentence
            example:
            required: false
            selector:
                text:    
    """

    # https://developers.home-assistant.io/docs/dev_101_config
    language = hass.config.language if hass.config.language != None else "en"
    filename = hass.config.config_dir + "/custom_sentences/" + language + "/" + custom + ".response.yaml"

     # fallback: if the preferred language file does not exist use the 'en' version
    if not os.path.exists(filename):
        filename = hass.config.config_dir + "/custom_sentences/" + "en" + "/" + custom + ".response.yaml"

    sentence, exception = read_response(intent, response, filename)

    if exception:
        errno, strerror = exception.args
        response_variable = {"error": errno, "message": strerror}
        return response_variable
    
    try:
        sentence = sentence.replace("{{", "{").replace("}}","}").replace("{ ", "{").replace(" }", "}")
        sentence = sentence.format(**kwargs)
        response_variable = {"error": 0, "message": sentence}
        return response_variable
    except KeyError:
        message = "Matching Error: " + sentence
        response_variable = {"error": 1, "message": message}
        return response_variable
