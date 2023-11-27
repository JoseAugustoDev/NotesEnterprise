from Flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('html/login.html')