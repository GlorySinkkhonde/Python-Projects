# Get password length

# Use it to generate random combination of text containing , letters, numbers and symbols

# store the value in a variable

# display the generated password on generated password input



from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return ("hello world")

@app.route("/generator", methods=["POST"])
def users():
    print("users endpoint reached...")
    data = request.json
    password_length = data.get("passwordLength")
    print("Received password length:", password_length)

    return jsonify({"message": "Data received successfully"})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True)

