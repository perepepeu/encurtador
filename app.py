from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)
links = {}

def gerar_codigo(tamanho=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_link = None
    if request.method == 'POST':
        url_original = request.form['url']
        codigo = gerar_codigo()
        links[codigo] = url_original
        short_link = request.host_url + codigo
    return render_template('index.html', short_link=short_link)

@app.route('/<codigo>')
def redirecionar(codigo):
    url = links.get(codigo)
    if url:
        return render_template('wait.html', url=url)
    else:
        return "Link inválido!", 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
