# Reads some text and automatically creates quiz questions based on keywords it finds

def generate_quiz_questions(text):
    questions = []

    concepts = [
                "Artificial Intelligence",
                "Machine Learning",
                "Supervised Learning",
                "Unsupervised Learning",
                "Reinforcement Learning"
                ]

    for concept in concepts:
        if concept.lower() in text.lower():
            questions.append(f"What is {concept}?")

    if not questions:
        questions.append("What are the main ideas from these notes?")

    return questions
