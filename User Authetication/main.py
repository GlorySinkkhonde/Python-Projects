'''
--- User login ---

Get user data

Check if it exists in database

let them in

--- user sign up ---

Get their data

Post to database

'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
