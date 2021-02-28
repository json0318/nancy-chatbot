from flask import render_template, flash, jsonify, url_for, request
from app import app
from app.core_nancy import predict

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'visitor'}

    return render_template('index.html', title='Home', user=user)

@app.route('/chat', methods=['POST'])
def chat():
    result = "NANCY: " + predict(request.form['msg'])
    msg = "<div>"+request.form['username']+": "+request.form['msg']+"</div><div>"+result+"</div>"

    return msg
