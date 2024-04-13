from flask import Flask, render_template, request, send_file
import requests

# Peticion a api para obtener trabajos
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

def jobs_json():
        return {
  "jobs": [
    {
      "id": 1,
      "title": "Trabajo 1",
      "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Reiciendis ducimus temporibus placeat sequi exercitationem odit illo sapiente cupiditate. Quisquam eveniet corrupti officiis voluptates deleniti sapiente libero voluptatum? Quasi, tempore placeat.",
      "employmentType": "Remoto",
      "jobProviders": [
        {
          "url": "",
          "jobProvider": "proveedor1"
        },
        {
          "url": "",
          "jobProvider": "proveedor1"
        },
        {
          "url": "",
          "jobProvider": "proveedor2"
        },
        {
          "url": "",
          "jobProvider": "proveedor3"
        }
      ]
    },
    {
      "id": 1,
      "title": "Trabajo 2",
      "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Reiciendis ducimus temporibus placeat sequi exercitationem odit illo sapiente cupiditate. Quisquam eveniet corrupti officiis voluptates deleniti sapiente libero voluptatum? Quasi, tempore placeat.",
      "employmentType": "Remoto",
      "jobProvider": [
        {
          "url": "",
          "jobProvider": "proveedor1"
        },
        {
          "url": "",
          "jobProvider": "proveedor1"
        },
        {
          "url": "",
          "jobProvider": "proveedor2"
        },
        {
          "url": "",
          "jobProvider": "proveedor3"
        }
      ]
    },
    {
      "id": 1,
      "title": "Trabajo 3",
      "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Reiciendis ducimus temporibus placeat sequi exercitationem odit illo sapiente cupiditate. Quisquam eveniet corrupti officiis voluptates deleniti sapiente libero voluptatum? Quasi, tempore placeat.",
      "employmentType": "Remoto",
      "jobProvider": [
        {
          "url": "",
          "jobProvider": "proveedor1"
        },
        {
          "url": "",
          "jobProvider": "proveedor1"
        },
        {
          "url": "",
          "jobProvider": "proveedor2"
        },
        {
          "url": "",
          "jobProvider": "proveedor3"
        }
      ]
    }
  ]
}


app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        query = request.form['search']
        location = "Colombia"
        lang = "es"
        datePosted = "month"
        response = search_jobs(query, location, lang, datePosted)
        jobs = response['jobs']
        return render_template('index.html', jobs=jobs, query=query)
    jobs = jobs_json()
    query = ""

    return render_template('index.html', jobs=jobs['jobs'], query=query)

if __name__ == '__main__':
    app.run(debug=True)