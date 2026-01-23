import requests, re

@service(supports_response="optional")
def search_wikipedia(searchterm=None, language="en"):
    """yaml
    name: View Assist Search Wikipedia
    description: Search Wikipedia using searchterm in the specified language
    fields:
        searchterm:
            description: What to search for?
            example: Madonna
            required: true
            selector:
                text:
        language:
            description: Language code for the Wikipedia edition (e.g., 'en' for English, 'it' for Italian)
            example: en
            required: false
            default: en
            selector:
                text:
    """
    if searchterm is None:
        return {"error": "Missing searchterm"}

    # Construct the URL with the specified language
    url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{searchterm.replace(' ', '_')}?redirect=true"
    
    # Custom User-Agent (required!)
    headers = {
        "User-Agent": "HA-WikipediaSearch/1.0 (HomeAssistant pyscript; your.email@example.com)"
    }
    
    r = task.executor(requests.get, url, headers=headers)

    if r.status_code == requests.codes.ok:
        wiki_data = r.json()
        type_ = wiki_data.get('type', 'unknown')
        title = wiki_data.get('title', searchterm)
        try:
            thumbnail = wiki_data['thumbnail']['source']
        except (KeyError, TypeError):
            thumbnail = ""

        full_extract = wiki_data.get('extract', '')
        if full_extract:
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', full_extract.strip())
            extract = ' '.join(sentences[:2])
        else:
            extract = ""

        return {"type": type_, "title": title, "thumbnail": thumbnail, "extract": extract}
    else:
        try:
            error_data = r.json()
        except:
            error_data = r.text or "No response"
        return {"error": f"HTTP {r.status_code}", "details": error_data}
