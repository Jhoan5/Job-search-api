from flask import Flask, render_template, request, send_file
from . import api_jobs
from . import api_fake_jobs

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST' and len(request.form['search']) > 1:
        text = request.form['search']
        return render_template('ofertas.html', query=text)
    datos = api_fake_jobs.data()
    return render_template('index.html', datos=datos)
@app.route('/fake_response.json')
def serve_json():
    try:
        # Ruta al archivo JSON local
        ruta_archivo = 'fake_response.json'

        # Utiliza Flask's send_file para enviar el archivo JSON
        return send_file(ruta_archivo, mimetype='application/json')

    except Exception as e:
        # Si hay un error, devuelve un mensaje de error
        return f"Error: {str(e)}"

@app.route('/ofertas', methods=('GET', 'POST'))
def ofertas():
    if request.method == 'POST':
        query = request.form['search']
        location = "Colombia"
        lang = "es"
        datePosted = "month"
        response = api_jobs.search_jobs(query, location, lang, datePosted)
        jobs = response['jobs']
        return render_template('ofertas.html', jobs=jobs, query=query)
    return render_template('ofertas.html')

if __name__ == '__main__':
    app.run(debug=True)
