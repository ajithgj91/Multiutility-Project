from flask import Flask, request, render_template, jsonify
from textblob import TextBlob
import language_tool_python
from email_generator import generate_email_body

app = Flask(__name__)
tool = language_tool_python.LanguageTool('en-US')

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/index')
def sample():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index1.html')

@app.route('/text_correction')
def text_correction():
    return render_template('index.html')

@app.route('/text_to_audio')
def text_to_audio():
    return render_template('index2.html')

@app.route('/email_generator')
def email_generator():
    return render_template('index3.html')

@app.route('/generate', methods=['POST'])
def generate():
    subject = request.form['subject']
    email_body = generate_email_body(subject)
    return render_template('index3.html', email_body=email_body)

@app.route('/check', methods=['POST'])
def check_text():
    text = request.form['text']
    corrected_text = correct_text(text)
    return jsonify({'corrected_text': corrected_text})

def correct_text(text):
    # Spell check using TextBlob
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    
    # Grammar check using LanguageTool
    matches = tool.check(corrected_text)
    corrected_text = language_tool_python.utils.correct(corrected_text, matches)
    return corrected_text

if __name__ == '__main__':
    app.run(debug=True)
