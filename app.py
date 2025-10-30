from flask import Flask, render_template, request
from mvp.text_summarizer import summarize_text
from mvp.text_paraphraser import paraphrase_text
from mvp.text_sentiment import get_sentiment
from config_manager import load_config

app = Flask(__name__)
config = load_config()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['input_text']
    task = request.form['task']

    if task == 'summarize':
        output = summarize_text(text, config['summarization'])
    elif task == 'paraphrase':
        output = paraphrase_text(text, config['paraphrasing'])
    elif task == 'sentiment':
        output = get_sentiment(text, config['sentiment'])
    else:
        output = "Invalid option selected."

    return render_template('index.html', input_text=text, output_text=output)

if __name__ == '__main__':
    app.run(debug=True)