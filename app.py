from flask import Flask, render_template, redirect, url_for, request
import requests, json
import time

app = Flask(__name__)

#when play is pressed
@app.route("/", methods=['GET','POST'])
def index():

    return render_template('index.html')

@app.route("/page2")
def page2():
    return

if __name__ == '__main__':
    app.run(debug=True)