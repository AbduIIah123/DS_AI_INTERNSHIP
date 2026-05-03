from flask import Flask, jsonify, request

app = Flask(__name__)

# GET route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# POST route
@app.route('/data', methods=['POST'])
def receive_data():
    body = request.get_json()
    return jsonify({"you_sent": body}), 201

if __name__ == '__main__':
    app.run(debug=True)