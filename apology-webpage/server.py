"""
Flask server for the heartfelt apology web page.
-----------------------------------------------
To run the server:
1. Make sure Flask is installed:  pip install flask
2. Run this file:  python server.py
3. Open your browser and go to:  http://127.0.0.1:5000
"""

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def js():
    return send_from_directory('.', 'script.js')

if __name__ == '__main__':
    app.run(debug=True)
