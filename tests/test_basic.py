from app.summarizer import generate_summary
from app.quiz import generate_quiz_questions
from app.flashcards_generator import generate_flashcards

def test_generate_summary():
    text = "Python is a programming langauge. It is popular for AI. It is easy to learn."
    summary = generate_summary(text, max_sentences=2)

    assert summary == "Python is a programming langauge, It is popular for AI."

def test_generate_quiz_questions():
    text = "Machine Learning is a subset of Artificial Intelligence. "
    questions = generate_quiz_questions(text)

    assert "What is Machine Learning?" in questions
    assert "What is Artificial Intelligence?" in questions

def test_generate_flashcards():
    text = "Natural Language Processing is part of Artificial Intelligence."
    flashcards = generate_flashcards(text)

    assert len(flashcards) > 0