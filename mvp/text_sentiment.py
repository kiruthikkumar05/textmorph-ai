from transformers import pipeline

def get_sentiment(text, config):
    if not text.strip():
        return "Please enter text for sentiment analysis."

    sentiment_analyzer = pipeline("sentiment-analysis", model=config['model'])
    result = sentiment_analyzer(text)[0]
    return f"Sentiment: {result['label']} (Confidence: {result['score']:.2f})"