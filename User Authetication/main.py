from flask import Flask, jsonify, render_template, request, session, redirect, url_for
import bcrypt

app = Flask(__name__)
app.secret_key = b"76sdf"

users = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
        
    elif request.method == "POST":
        data = request.json
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        
        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        session['username'] = username
        session['email'] = email
        session['password'] = hashed_password
        
        # Add user to database
        users.append({
            "username": username,
            "email": email,
            "password": hashed_password
        })
        
        return jsonify("Registration successful")

@app.route('/login', methods=["GET", "POST"])
def log_in():
    if request.method == "GET":
        return render_template('login.html')
        
    elif request.method == "POST":
        data = request.json
        username = data.get("username")
        password = data.get("password")
    
    # Check if the username exists in the database
    for user in users:
        if user["username"] == username:
            stored_password = user["password"]
            # Check if the entered password matches the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                # Store user data in session after successful login
                session['logged_in'] = True
                session['username'] = username
                return jsonify("Login successful")
    
    return jsonify("Error: Invalid username or password")

@app.route('/account')
def account():
    # Check if user is logged in
    if 'logged_in' in session:
        return render_template('account.html')
    else:
        # Redirect to login page if user is not logged in
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
