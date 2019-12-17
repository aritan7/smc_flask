from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['post'])
def register():
    name = request.form.get("name")
    session = request.form.get("session")
    print(name, session)
    if not name or not session:
        return "Failure"
    return render_template('success.html')
