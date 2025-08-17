from transformers import pipeline
import config

summarizer = pipeline("summarization", model=config.SUMMARIZATION_MODEL)

def summarize_text(text, max_words=200):
    summary = summarizer(text, max_length=max_words, min_length=50, do_sample=False)
    return summary[0]['summary_text']
