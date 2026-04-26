# Scans text for predefined concepts and generates matching flashcards based on keyword detection

def generate_flashcards(text):
    flashcards = []

    concepts = {
        "Artificial Intelligence": "A field of computer science focused on creating systems that perform tasks requiring human intelligence.",
        "Machine Learning": "A subset of AI that allows computers to learn from data.",
        "Natural Language Processing": "A branch of AI that helps computers understand, interpret, and generate human language.",
        "supervised learning": "A type of machine learning where a model learns from labeled data.",
        "unsupervised learning": "A type of machine learning where a model finds patterns in unlabeled data.",
        "reinforcement learning": "A type of machine learning where an agent learns by receiving rewards or penalties."
        }

    for term, definition in concepts.items():
        if term.lower() in text.lower():
            flashcards.append( (term, definition) )

    return flashcards