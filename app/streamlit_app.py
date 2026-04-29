import streamlit as st

from ai_generator import generate_ai_study_material
from pdf_reader import extract_text_from_pdf
from summarizer import generate_summary
from quiz import generate_quiz_questions
from flashcards_generator import generate_flashcards

st.set_page_config(
    page_title = "AI Study Assistant",
    page_icon = "🤖📚",
    layout = "centered"
)

st.title("AI Study Assistant")
st.write("Upload PDF notes or paste text to generate summaries, quiz questions, flashcards and revision checklists.")

input_method = st.radio(
    "Choose input method:",
    ["Paste text", "Upload PDF"]
)

notes = ""

if input_method == "Paste text":
    notes = st.text_area(
        "Paste your study notes here:",
        height=300,
        placeholder="Paste lecture notes, textbook notes, or revision materials..."
    )
else:
    uploaded_file = st.file_uploader(
        "Upload a PDF file:",
        type=["pdf"]
    )
    if uploaded_file is not None:
        notes = extract_text_from_pdf(uploaded_file)
        st.success("PDF text extracted successfully.")

        with st.expander("Preview extracted text"):
            st.write(notes[:3000])

mode = st.selectbox(
    "Choose generation mode:",
    ["AI-powered", "Basic rule-based"]
)

if st.button("Generate Study Material"):
    if not notes.strip():
        st.warning("Please provide notes first.")
    else:
        with st.spinner("Generating study material..."):
            if mode == "AI-powered":
                result = generate_ai_study_material(notes)
            else:
                summary = generate_summary(notes)
                questions = generate_quiz_questions(notes)
                flashcards = generate_flashcards(notes)

                result = "# Summary\n"
                result += summary + "\n"

                result += "# Quiz Questions\n"
                for index, question in enumerate(questions, start=1):
                    result += f"{index}. {question}\n"

                result += "\n# Flashcards\n"
                for term, definition in flashcards:
                    result += f"Q: What is {term}? \n A: {definition}\n\n"

        st.subheader("Generated Study Material")
        st.markdown(result)

        st.download_button(
            label = "Download as Markdown",
            data = result,
            file_name = "study_material.md",
            mime = "text/markdown"
        )



