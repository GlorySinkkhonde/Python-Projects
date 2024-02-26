
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import string

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return ("hello world")

@app.route("/generator", methods=["GET", "POST"])
def generator():
    if request.method == "GET":
        return "This is the generator end."
    elif request.method == "POST":
        data = request.json
        password_length = data.get("passwordLength")
        print("Received password length:", password_length)
        
        #Create a list of letters
        #create a list of numbers
        #create a list of symbols
        #Then the password variable should mix different types of these and display them in the password length requested to the generated password input
        
        small_letters = [letter for letter in string.ascii_lowercase]
        capital_letters = [letter.upper() for letter in small_letters]
        numbers = [digit for digit in string.digits]
        symbols = []
        
        for ascii_value in range(33, 127):
            character = chr(ascii_value)
            if not character.isalnum():
                symbols.append(character)
        
        password = small_letters
        print(capital_letters)
        
        return jsonify(password)
    

if __name__ == '__main__':
    app.run(debug=True)

