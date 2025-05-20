from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')
CERT, KEY = 'ssl/cert.pem', 'ssl/key.pem'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    base = os.path.dirname(__file__)
    cert = os.path.join(base, CERT)
    key  = os.path.join(base, KEY)
    app.run(host='127.0.0.1', port=5000, ssl_context=(cert, key), debug=True)