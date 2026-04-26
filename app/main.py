from app.utils import read_text_file, save_output
from app.summarizer import generate_summary
from app.quiz import generate_quiz_questions
from app.flashcards_generator import generate_flashcards

def main():
    input_path = "data/sample_notes.txt"
    output_path = "outputs/study_output.txt"

    text = read_text_file(input_path)

    summary = generate_summary(text)
    quiz_questions = generate_quiz_questions(text)
    flashcards = generate_flashcards(text)

    output = "AI Study Assistant Output\n"
    output += "=" * 30 + "\n\n"

    output += "Summary: \n"
    output += summary + "\n\n"

    output += "Quiz Questions: \n"
    for index, question in enumerate(quiz_questions, start=1):
        output += f"{index}/ {questions}\n"

    output += "\nFlashcards:\n"
    if flashcards:
        for term, definition in flashcards:
            output += f"- {term}: {definition}\n"
    else:
        output += "No flashcards generated.\n"

    save_output(output_path, output)

    print("Study output generated successfully!")
    print(f"Saved to: {output_path}")

    if __name__ == "__main__":
        main()