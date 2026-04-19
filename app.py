# Import required Flask modules

from flask import Flask, render_template, request

# Import our custom AI logic from ai_tools folder
from ai_tools.summarizer import summarize_pdf
from ai_tools.pdf_chatbot import ask_question_about_pdf
from ai_tools.handwriting import convert_handwriting_image
from ai_tools.resume_analyzer import analyze_resume
from ai_tools.grammer import correct_grammar

# Initialize the Flask app
app = Flask(__name__)

# -------------------------------
# Route: Homepage (navigation UI)
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')  # renders main menu HTML


# ---------------------------------------
# Route: PDF Summarizer tool (/summarizer)
# Handles GET (open form) & POST (submit PDF)
# ---------------------------------------
@app.route('/summarizer', methods=['GET', 'POST'])
def summarizer():
    summary = ""
    if request.method == 'POST':
        pdf = request.files['pdf']  # get uploaded PDF
        summary = summarize_pdf(pdf)  # call AI logic to summarize
    return render_template('summarizer.html', summary=summary)


# ------------------------------------------
# Route: PDF Chatbot (Question Answering on PDF)
# ------------------------------------------
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    answer = ""
    if request.method == 'POST':
        pdf = request.files['pdf']
        question = request.form['question']  # get user question
        answer = ask_question_about_pdf(pdf, question)  # call AI logic
    return render_template('chatbot.html', answer=answer)


# -------------------------------------------------
# Route: Handwriting to Text Converter (/handwriting)
# -------------------------------------------------
@app.route('/handwriting', methods=['GET', 'POST'])
def handwriting():
    result = ""
    if request.method == 'POST':
        image = request.files['image']  # uploaded handwritten image
        result = convert_handwriting_image(image)  # call AI OCR logic
    return render_template('handwriting.html', result=result)


# ------------------------------------------
# Route: Resume Analyzer (/resume)
# ------------------------------------------
@app.route('/resume', methods=['GET', 'POST'])
def resume():
    result = {}
    if request.method == 'POST':
        pdf = request.files['pdf']  # get uploaded resume PDF
        result = analyze_resume(pdf)  # call AI logic to analyze resume
    return render_template('resume.html', result=result)


# ----------------------------------
# Route: Grammar Checker (/grammar)
# ----------------------------------
@app.route('/grammar', methods=['GET', 'POST'])
def grammar():
    result = ""
    error = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        output = correct_grammar(text)
        if isinstance(output, dict) and output.get('error'):
            error = output['error']
        else:
            result = output
    return render_template('grammar.html', result=result, error=error)


# ----------------------------------
# Route: Get Started (/getstarted)
# ----------------------------------
@app.route('/getstarted')
def getstarted():
    return render_template('getstarted.html')


# ------------------------------------------

# Start the Flask app
# ---------------------
if __name__ == '__main__':
    app.run(debug=True)
