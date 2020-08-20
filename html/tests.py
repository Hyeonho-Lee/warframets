from flask import Flask, url_for, render_template, request, redirect, session
import sys

app = Flask(__name__)

@app.route("/")
def hey():
    return "hey"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(sys.argv[1]))