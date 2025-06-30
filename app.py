from flask import Flask, request, jsonify
from auth import verify_api_key
from crypto_utils import generate_aes_key

app = Flask(__name__)

# Middleware de verificação de API Key
@app.before_request
def check_api_key():
    if not verify_api_key(request):
        return jsonify({"error": "API Key inválida"}), 403

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "API está ativa e protegida"}), 200

@app.route('/generate-key', methods=['POST'])
def generate_key():
    key = generate_aes_key()
    return jsonify({"key": key.hex()}), 200

if __name__ == '__main__':
    app.run(debug=True)
