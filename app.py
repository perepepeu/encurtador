from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)
short_to_url = {}

def generate_short_link():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_link = generate_short_link()
        short_to_url[short_link] = original_url
        return render_template('index.html', short_link=request.host_url + short_link)
    return render_template('index.html')

@app.route('/<short_link>')
def redirect_to_url(short_link):
    original_url = short_to_url.get(short_link)
    if original_url:
        return redirect(original_url)
    return "Link inválido.", 404

if __name__ == '__main__':
    app.run(debug=True)
