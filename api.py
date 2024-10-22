from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-python', methods=['POST'])

@app.route('/hello', methods=['GET'])
def run_python():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
