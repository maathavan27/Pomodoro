from flask import Flask, render_template, redirect, url_for
import requests, json
app = Flask(__name__)

mins = 25
sec = "00"

def start():
    print("hi")

@app.route("/")
def main():
    return render_template('index.html', minute = mins, seconds = sec)

@app.route("/page2")
def page2():
    return

if __name__ == '__main__':
    app.run(debug=True)