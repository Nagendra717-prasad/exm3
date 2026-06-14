from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = requests.get('http://backend:8080')  # Call backend service
    return f"Frontend says: {response.text}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
