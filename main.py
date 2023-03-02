# -*- coding: utf-8 -*-

from docx import Document
import os

# Scripts
from get_inputs import capture_openAI_model, capture_syllabus_selected_section
from manage_files import read_docx, read_pdf, write_html_history, read_syllabus_HTML
from openai import call_openAI_API

# Given a string, trims it to a given length

def trim_text(text, length):
    preprocess_text = text.replace("\n", " ")
    trims = [(preprocess_text[i:i + length])
             for i in range(0, len(text), length)]
    return trims[0]

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



if __name__ == "__main__":

    print("\n\n~~___Running___~~\n\n")

    # 1. Capturar y almacenar la sección del syllabus que se desea usar
    syllabus_selected_section = capture_syllabus_selected_section()

    # 2. Leer el HTML del syllabus y almacenarlo en una variable
    syllabus_virtual_document = read_syllabus_HTML()

    # 3. Capturar que modelo de OpenAI (Copletion, Edition) desea usar
    openai_model = capture_openAI_model()

    # 4. Capturar las instrrucciones para la IA
    openai_prompt = input(
        "\nType something to do with the text: \nR:")

    # 5. Extraer la sección del texto seleccionado del syllabus
    openai_text = syllabus_virtual_document.find(
        syllabus_selected_section).text

    # # # 6. Llamar la API de OpenAI
    # openAI_response = call_openAI_API(
    #     openai_prompt, openai_model, openai_text, syllabus_selected_section)
    
    # 7. reconstructiong the virtual syllabus with the API response
    syllabus_virtual_document.find(syllabus_selected_section).string = "cambio"

    write_html_history(syllabus_virtual_document, openai_model, syllabus_selected_section)
   
