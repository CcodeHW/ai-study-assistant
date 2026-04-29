import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_study_material(notes: str) -> str:
    if not notes.strip():
        return "No notes provided."

    prompt = f"""
You are an AI study assistant for university students.

Create useful study material from the notes below.

Return the result in this exact structure:

# Summary
Write a clear student-friendly summary.

# Key Concepts
List the most important concepts with short explanations.

# Quiz Questions
Create 5 quiz questions.

# Flashcards
Create 5 flashcards in this format:
Q: ...
A: ...

# Revision Checklist
Create a checklist students can use before an exam

Notes:
{notes}
"""
    response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt,
    )

    return response.output_text





