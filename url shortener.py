from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(_name_)
url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_url = generate_short_url()
    url_mapping[short_url] = original_url
    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found."

if _name_ == '_main_':
    app.run(debug=True)
