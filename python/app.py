from Flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('/index.html')

@app.route('/login')
def login_page():
    return render_template('/html/login.html')

@app.route('/main')
def main_page():
    return render_template('/html/main.html')