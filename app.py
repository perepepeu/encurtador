from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

# Dicionário para armazenar URLs encurtadas
url_db = {}

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({'error': 'URL não fornecida'}), 400

    # Gerar uma chave curta única
    short_key = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    short_url = f"http://localhost:5000/{short_key}"

    # Salvar no banco de dados
    url_db[short_key] = original_url

    return jsonify({'shortUrl': short_url})

@app.route('/<short_key>', methods=['GET'])
def redirect_url(short_key):
    original_url = url_db.get(short_key)
    if original_url:
        return f'<script>window.location.href="{original_url}";</script>'
    return jsonify({'error': 'URL não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)