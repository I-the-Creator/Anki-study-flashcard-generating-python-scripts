import docx

def convert_to_txt(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + '\n'
    with open('file.txt', 'w') as f:
        f.write(text)

file_path = 'path/to/file.docx'
convert_to_txt(file_path)
