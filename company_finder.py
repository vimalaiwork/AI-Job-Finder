from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

def find_companies(location, domain):

    query = f"{domain} companies in {location}"

    run_input = {
        "searchStringsArray": [query],
        "maxCrawledPlacesPerSearch": 5
    }

    run = client.actor(
        "compass/crawler-google-places"
    ).call(run_input=run_input)

    companies = []

    for item in client.dataset(
        run["defaultDatasetId"]
    ).iterate_items():

        companies.append({
            "name": item.get("title"),
            "address": item.get("address"),
            "rating": item.get("totalScore")
        })

    return companies