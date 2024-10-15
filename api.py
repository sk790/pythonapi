from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])
def run_python():
    data = request.json
    name = data.get('name', 'User')
    return jsonify(message=f"Hello, {name}!")
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=5000)
