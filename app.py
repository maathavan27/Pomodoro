from flask import Flask, render_template, redirect, url_for, request, send_file
import requests, json
import time

app = Flask(__name__)

#when play is pressed
@app.route("/", methods=['GET','POST'])
def index():

    return render_template('index.html')

@app.route("/notification.mp3")
def notification():
    return send_file('notification.mp3', attachment_filename='notification.mp3')

if __name__ == '__main__':
    app.run(debug=True)