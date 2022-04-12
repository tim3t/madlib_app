from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app=Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
# debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story')
def show_story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)