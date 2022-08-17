from ensurepip import bootstrap
from flask import Flask, render_template
import os

app=Flask(__name__)
pic = os.path.join('static')
app.config['UPLOAD FOLDER'] = pic


@app.route('/')
def index():
    code = os.path.join(app.config['UPLOAD FOLDER'], 'code.ico')
    bootstrap = os.path.join(app.config['UPLOAD FOLDER'], 'bootstrap.png')
    discord = os.path.join(app.config['UPLOAD FOLDER'], 'discord.png')
    duckduckgo = os.path.join(app.config['UPLOAD FOLDER'], 'duckduckgo.png')
    github = os.path.join(app.config['UPLOAD FOLDER'], 'github.png')
    search = os.path.join(app.config['UPLOAD FOLDER'], 'search.png')
    stack = os.path.join(app.config['UPLOAD FOLDER'], 'stack.png')
    youtube = os.path.join(app.config['UPLOAD FOLDER'], 'youtube.png')
    return render_template('index.html',code = code,discord = discord,github = github,search = search,stack = stack,youtube = youtube,duckduckgo = duckduckgo,bootstrap = bootstrap)

if __name__ == '__main__':

    app.run(debug=True)