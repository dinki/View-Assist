import aiohttp
import asyncio
from urllib.parse import quote
import re
import calendar
import requests
from datetime import datetime, timedelta

@service(supports_response="optional")
async def search_wikipedia(searchterm=None, language="en", return_response=True):
    """yaml
    name: View Assist Search Wikipedia
    description: Search Wikipedia using a search term
    fields:
        searchterm:
            description: What to search for?
            example: Madonna
            required: true
            selector:
                text:
        language:
            description: In what language to search?
            example: it
            required: true
            selector:
                text:
    """

    async def get_average_views(title, language='en'):
        # Encode the title for a valid URL
        title_url = quote(title)

        # Calculate the last 30 days from today (UTC)
        end_date_obj = datetime.utcnow().date()
        start_date_obj = end_date_obj - timedelta(days=30)

        # Format dates for the API (YYYYMMDD)
        start_date = start_date_obj.strftime("%Y%m%d")
        end_date = end_date_obj.strftime("%Y%m%d")

        # Wikimedia Pageviews API URL
        url = (
            f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
            f"{language}.wikipedia.org/all-access/all-agents/"
            f"{title_url}/daily/{start_date}/{end_date}"
        )

        headers = {
            "accept": "application/json",
            "User-Agent": "MyPythonScript/1.0"
        }

        # Make the API request
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    # Return 0 views if the request fails
                    return 0
                data = await response.json()

        # Extract views per day
        views = [item["views"] for item in data.get("items", [])]
        if not views:
            return 0
        # Return the average views
        return sum(views) / len(views)

    # Wikipedia summary REST API URL
    rest_url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{searchterm.replace(' ', '_')}?redirect=true"
    r = await task.executor(requests.get, rest_url)

    if r.status_code == 200:
        wiki_data = r.json()
        page_type = wiki_data.get('type', '')
        title = wiki_data.get('title', '')
        thumbnail = wiki_data.get('thumbnail', {}).get('source', '')
        full_extract = wiki_data.get('extract', '')

        # If the result is a disambiguation page
        if page_type == 'disambiguation':
            api_url = f"https://{language}.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "titles": title,
                "prop": "links",
                "pllimit": "max",
                "format": "json"
            }

            # Request the list of disambiguation links
            api_response = await task.executor(requests.get, api_url, params=params)
            if api_response.status_code == 200:
                api_data = api_response.json()
                pages = api_data.get('query', {}).get('pages', {})
                disambiguation_links = []

                # Get view stats for each disambiguation link
                for page in pages.values():
                    links = page.get('links', [])
                    for link in links:
                        link_title = link.get('title', '')
                        v = await get_average_views(link_title, language=language)
                        disambiguation_links.append({"link title": link_title, "views": v})

                # Sort by popularity and repeat the search with the top link
                disambiguation_links.sort(key=lambda x: x["views"], reverse=True)
                return search_wikipedia(disambiguation_links[0]["link title"], language=language)

            else:
                # Error fetching disambiguation links
                return {
                    "error": api_response.status_code,
                    "message": "Error while retrieving disambiguation links."
                }

        else:
            # Extract the first two sentences
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', full_extract.strip())
            extract = ' '.join(sentences[:2])
            return {
                "type": page_type,
                "title": title,
                "thumbnail": thumbnail,
                "extract": extract
            }

    else:
        # Error fetching the main Wikipedia summary
        return {
            "error": r.status_code,
            "message": "Error while retrieving data from Wikipedia."
        }
