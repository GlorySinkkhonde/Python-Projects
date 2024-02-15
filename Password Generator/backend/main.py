# Get password length

# Use it to generate random combination of text containing , letters, numbers and symbols

# store the value in a variable

# display the generated password on generated password input



from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "My first Python backend! H"

if __name__ == '__main__':
    app.run(debug=True)

