import requests

def search_jobs(query, location, lang, datePosted):
    url = "https://jobs-api14.p.rapidapi.com/list"

    querystring = {
        "query": query,
        "location": location,
        "distance": "1.0",
        "language": lang,
        "datePosted": datePosted,
        "employmentTypes": "fulltime;parttime;intern;contractor",
        "index": "0"
    }

    headers = {
        "X-RapidAPI-Key": "1b36c99d7dmshd9bfdc0ee6eececp104e5ajsn6bc4e59e68c5",
        "X-RapidAPI-Host": "jobs-api14.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

    return response.json()
