from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__) #referencing the file







@app.route('/')
def index():
    return "test"

if __name__ == "__main__":
    app.run(debug=True)