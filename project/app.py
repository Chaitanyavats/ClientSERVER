# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = [{'email': 'example@example.com', 'password': 'password'}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for user in users:
            if user['email'] == email and user['password'] == password:
                # Successful login
                return redirect(url_for('chatbox'))
        # Invalid credentials
        return "Invalid email or password"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users.append({'email': email, 'password': password})
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Implement logic to reset password
        return "Password reset link sent to your email"
    return render_template('forgot_password.html')

@app.route('/chatbox')
def chatbox():
    return render_template('chatbox.html')

if __name__ == '__main__':
    app.run(debug=True)