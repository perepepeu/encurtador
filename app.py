from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

links = {}

def gerar_codigo():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_original = request.form['url']
        codigo = gerar_codigo()
        links[codigo] = url_original
        return render_template('index.html', codigo=codigo)
    return render_template('index.html')

@app.route('/<codigo>')
def redirecionar(codigo):
    url = links.get(codigo)
    if url:
        return render_template('wait.html', url=url)
    else:
        return "Link inválido!", 404

if __name__ == '__main__':
    app.run()
