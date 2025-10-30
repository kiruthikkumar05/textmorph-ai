from transformers import pipeline

def paraphrase_text(text, config):
    if not text.strip():
        return "Please enter text to paraphrase."

    paraphraser = pipeline("text2text-generation", model=config['model'])
    para = paraphraser(f"paraphrase: {text}", max_length=config['max_length'], num_return_sequences=1, do_sample=True)
    return para[0]['generated_text']