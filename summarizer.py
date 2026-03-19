def summarize(text):
    # simple fallback summarization
    if len(text) < 100:
        return text
    return text[:100] + "..."