import requests
@service(supports_response="optional")
def viewassist_get_dadjoke(return_response=True):
    """yaml
    name: Get Dad joke
    description: Gets a random dad joke from api
    """
    url = "https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes"
    headers = {
    'x-rapidapi-key': "get your api key at rapidapi",
    'x-rapidapi-host': "dad-jokes-by-api-ninjas.p.rapidapi.com"
    }

    r = task.executor(requests.get, url, headers=headers)
  
    if r.status_code == requests.codes.ok:
        response_variable = r.json()
        return response_variable[0]
    else:
        response_variable = {"error": r.status_code, "data": r.json()}
