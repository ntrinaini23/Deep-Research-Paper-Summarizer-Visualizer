import requests
import config

def get_definition(term):
    url = config.WIKI_API_URL + term
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return data.get("extract", "No definition found.")
    return "No definition found."
