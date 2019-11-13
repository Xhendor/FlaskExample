from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hola mundo!!!!'
@app.route('/pagina')
def pagina():
    return render_template("login.html",coco="Soy el texto")