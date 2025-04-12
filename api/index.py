from flask import Flask, render_template

# 正确实例化 Flask 应用
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
