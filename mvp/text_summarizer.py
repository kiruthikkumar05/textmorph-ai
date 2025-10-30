from transformers import pipeline

def summarize_text(text, config):
    if not text.strip():
        return "Please enter text to summarize."

    summarizer = pipeline("summarization", model=config['model'])
    summary = summarizer(text, max_length=config['max_length'], min_length=config['min_length'], do_sample=False)
    return summary[0]['summary_text']