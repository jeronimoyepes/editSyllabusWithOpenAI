# -*- coding: utf-8 -*-

import docx
from docx import Document
import PyPDF2
import openai
import os

my_directory = os.path.dirname(__file__)

# Set OpenAI API key
openai.api_key = "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"

# Character's limit for openAI API
openai_maximum_content_length = 2049

# Trim text for OpenAI maximum context length
def trim_text(text_from_file):
    correct_text_length = openai_maximum_content_length - len(openai_prompt)
    preprocess_text = text_from_file.replace("\n", " ")
    trims = [(preprocess_text[i:i + correct_text_length])
             for i in range(0, len(text_from_file), correct_text_length)]
    return trims[0]

# Function to get text from Word document
def read_docx(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text_from_file)
    return '\n'.join(full_text)

# Function to get text from PDF
def read_pdf(filename):
    pdf_file = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    full_text = []
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        full_text.append(page_obj.extract_text())
    return '\n'.join(full_text).strip('\n')

# Function to get text from file
def get_text_from_file(file_to_read):
    # Get file extension
    file_extension = file_to_read.split('.')[-1].lower()

    # Read text from file based on extension
    if file_extension == 'docx' or file_extension == 'doc':
        extracted_text = read_docx(file_to_read)
        print("\n__Word document read__\n")
    elif file_extension == 'pdf':
        extracted_text = read_pdf(file_to_read)
        print("Reading PDF document")
    else:
        print('Unsupported file format')
        extracted_text = None
    return extracted_text

# Function to get openAI response
def call_openAI_API(prompt):
    print(
        f"\n__Calling OpenAI with the prompt:\n {prompt} \n\n End of prompt__ \n\n Waiting for OpenAI response...\n")
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Get openAI response text
    response = completions.choices[0].text
    # Clean up openAI response text
    response = response.replace('\n', ' ')
    response = response.replace('Syllabus:', '').strip()
    return response

# Function to write word document with given prompt and response
def write_docx(prompt, response):
    document = Document()
    document.add_heading("Documento generado automáticamente con el prompt:")
    document.add_paragraph(prompt)
    document.add_heading("Respuesta de OpenAI:")
    document.add_paragraph(response)
    document.save('OpenAI response.docx')

if __name__ == "__main__":

    
    # 1. Prompt para seleccionar la sección a usar
    # 2. Leer la estructura del html
    #   - Duplicar el archivo original (agregar fecha y hora)
    #   - Buscar el archivo
    #   - Verificar la integridad
    #   - Tomar solo la sección deseada
    # 3. Pedir el prompt del tipo de acción (Completar o editar)
    # 4. Hacer el llamado a la api
    # 5. Reconstruir el documento y guardarlo 
    

    # OpenAI prompt (What you want to do with de text_from_file)
    openai_prompt = input("Type something to do with the document: ") + " from the following text:"

    # Docx filename
    file_name = input("Write the file name: ") or "defaultfile.pdf"

    # Concat filename with directory path
    file_path = os.path.join(my_directory, file_name)

    # Check if file exists
    if file_path and os.path.exists(file_path):
        print("\n\n~~___Running___~~\n\n")
        print(f"File path: {file_path}\n")

        text_from_file = get_text_from_file(file_path)
        
        if text_from_file:

            # Generate the prompt for the OpenAI API
            prompt = (f"{openai_prompt}\n\n{trim_text(text_from_file)}")
            openAI_response = call_openAI_API(prompt)
            print(f"\n\n __OpenAI response:__ \n\n{openAI_response}\n")

            # Write word document with the OpenAi Response
            write_docx(prompt, openAI_response)
            print("\n\n~~___Finished___~~\n\n")
    else:
        print("File does not exist")
