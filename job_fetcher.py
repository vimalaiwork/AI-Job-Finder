from apify_client import ApifyClient
from config import APIFY_TOKEN

client = ApifyClient(APIFY_TOKEN)

def fetch_jobs(role, location):

    run_input = {
        "position": role,
        "location": location,
        "maxItems": 10
    }

    run = client.actor(
        "misceres/indeed-scraper"
    ).call(run_input=run_input)

    jobs = []

    for item in client.dataset(
        run["defaultDatasetId"]
    ).iterate_items():

        jobs.append({
            "title": item.get("positionName"),
            "company": item.get("company"),
            "location": item.get("location"),
            "salary": item.get("salary")
        })

    return jobs