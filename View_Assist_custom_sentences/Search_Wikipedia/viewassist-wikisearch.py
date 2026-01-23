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

    # Custom User-Agent (required!)
    headers = {
        "User-Agent": "HA-WikipediaSearch/1.0 (HomeAssistant pyscript; your.email@example.com)"
    }

    # Step 1: Search Wikipedia to resolve canonical page title
    search_url = f"https://{language}.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": searchterm,
        "format": "json"
    }

    search_r = task.executor(
        requests.get,
        search_url,
        params=search_params,
        headers=headers
    )

    if search_r.status_code != requests.codes.ok:
        return {"error": "Search failed", "details": search_r.text}

    search_data = search_r.json()
    search_results = search_data.get("query", {}).get("search", [])

    if not search_results:
        return {"error": "No results found"}

    # Use canonical Wikipedia title from search result
    page_title = search_results[0]["title"]

    # Step 2: Construct summary URL using canonical title
    url = (
        f"https://{language}.wikipedia.org/api/rest_v1/page/summary/"
        f"{page_title.replace(' ', '_')}?redirect=true"
    )
    
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
