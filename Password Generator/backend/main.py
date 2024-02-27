# Get password length

# Use it to generate random combination of text containing , letters, numbers and symbols

# store the value in a variable

# display the generated password on generated password input

from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import string
import random

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
        password_length = int(data.get("passwordLength"))
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
        
        characters = small_letters + capital_letters + numbers + symbols
              
                #Return number of letters equal to the password length
                #return a mixture of numbers, letters and symbols
                
        def generate_password(length):
            password=''
            while len(password) < length:
                password += random.choice(characters)
            return password[:length]
        
        password = generate_password(password_length)
        
        #Once password is accepted, copy to clipboard (use JS)
        
        return jsonify(password)
    

if __name__ == '__main__':
    app.run(debug=True)

