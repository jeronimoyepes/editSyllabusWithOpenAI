import os
import docx, PyPDF2
from bs4 import BeautifulSoup

# Función para leer XML (HTML)
def BS(markup):
    return BeautifulSoup(markup, "lxml")

# Write HTMl documents after OpenAI response
def write_html_history(xml, model, section) :

    # Count amount of files in ./history folder to asign a version number in file name
    count = 0
    # Iterate directory
    for path in os.listdir(r'history/'):
        # check if current path is a file
        if os.path.isfile(os.path.join(r'history/', path)):
            count += 1

    history_file_name = f'history/v{count}-Syllabus_{section}_{model}.html'
    with open(history_file_name, "w", encoding="UTF-8") as file:
        file.write(str(xml))


# Read the syllabus in ./syllabus folder
def read_syllabus_HTML():
    with open(r"syllabus/originalSyllabus.html", encoding="UTF-8") as html_doc:
        return BS(html_doc)

# Get text from Word document
def read_docx(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text_from_file)
    return '\n'.join(full_text)

# Get text from PDF
def read_pdf(filename):
    pdf_file = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    full_text = []
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        full_text.append(page_obj.extract_text())
    return '\n'.join(full_text).strip('\n')

# Write word documents 
def write_docx(prompt, response):
    document = docx.Document()
    document.add_heading("Documento generado automáticamente con el prompt:")
    document.add_paragraph(prompt)
    document.add_heading("Respuesta de OpenAI:")
    document.add_paragraph(response)
    document.save('OpenAI response.docx')