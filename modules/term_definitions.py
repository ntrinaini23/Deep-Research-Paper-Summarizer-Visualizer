import requests
from config import WIKIPEDIA_API_URL

def get_definition(term):
    """
    Fetch a brief definition of a term from Wikipedia.
    """
    try:
        url = f"{WIKIPEDIA_API_URL}{term}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", f"No definition found for {term}.")
        else:
            return f"No definition found for {term}."
    except Exception as e:
        return f"Error fetching definition for {term}: {e}"

def get_definitions_for_terms(terms):
    """
    Get definitions for multiple terms and return as a dictionary.
    """
    return {term: get_definition(term) for term in terms}
