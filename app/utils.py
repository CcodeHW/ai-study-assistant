# Given a file path, open the file, read everything inside it and return the content

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def save_output(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)