import pyjokes

@service(supports_response="optional")
def viewassist_get_joke(language="en", return_response=True):
    """yaml
        name: Get Random Joke
        description: "Gets a random joke from pyjokes in the selected language"
        fields:
            language:
                description: "Language code for the joke (supported: en, de, es, it, fr, gl, eu, ru)"
                example: it
                required: true
                selector:
                    text:
    """
    try:
        joke = pyjokes.get_joke(language=language)
        return {"joke": joke}
    except Exception as e:
        return {"error": str(e)}
