from flask import Flask,render_template

app = Flask()
@app.get('/')
def home():
    return render_template('home.html') 

