# Take a long piece of text and shorten it by keeping only the first few sentences

def generate_summary(text, max_sentences = 3):
    sentences = text.split(".")
    cleaned_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if not cleaned_sentences:
        return "No Text Available to Summarize."

    summary = cleaned_sentences[: max_sentences]
    return ". ".join(summary) + "."