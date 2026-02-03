import requests

@service(supports_response="optional")
def viewassist_wolfram_short_answer(query=None, return_response=True):
    """yaml
    name: Get short answer
    description: Gets a response from Wolfram Alpha's Short Answers API
    fields:
      query:
        description: query to be submitted to short answers API
        example: Convert 2 Tablespoons to teaspoons
        required: true
    """
    appid = "<your app id here>" # see https://products.wolframalpha.com/short-answers-api/documentation
    parameters = {
        "appid": appid,
        "i": query
    }
    url = "https://api.wolframalpha.com/v1/result"

    r = task.executor(requests.get, url, params=parameters)
  
    if r.status_code == requests.codes.ok:
        response_variable = {"response": r.text}
        return response_variable
    else:
        response_variable = {"error": r.status_code, "data": {"response": r.text}}
        return response_variable
