import os
from flask import Flask, render_template, send_from_directory, request, redirect
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html', title="MLH Fellow - Team 3", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('aboutPage.html', title="MLH Fellow - Team 3", url=os.getenv("URL"))

@app.route('/blog')
def blog():
    return render_template('blogPage.html', title="MLH Fellow - Team 3", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projectsPage.html', title="MLH Fellow - Team 3", url=os.getenv("URL"))
