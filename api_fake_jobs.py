import requests

def data():
    try:
        # Ruta al archivo JSON local
        ruta_archivo = 'http://127.0.0.1:5000/fake_response.json'

        response = requests.get(ruta_archivo)

        # Verificar el estado de la respuesta
        if response.status_code == 200:
            return response.text
        else:
            # Si la solicitud no tiene éxito, mostrar el código de estado
            return f"Error: {response.status_code}"
    except Exception as e:
        # Capturar cualquier excepción y mostrarla
        return f"Error: {str(e)}"
