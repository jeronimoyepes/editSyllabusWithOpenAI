# -*- coding: utf-8 -*-

# Scripts
from get_inputs import capture_openAI_model, capture_syllabus_selected_section, capture_boolean
from manage_files import read_docx, read_pdf, write_docx, write_html_history, read_syllabus_HTML
from openai_API import call_openAI_API

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

    # 6. Call OpenAI API
    openAI_response = call_openAI_API(
        openai_prompt, openai_model, openai_text, syllabus_selected_section)

    # 7. reconstructiong the virtual syllabus with the API response
    syllabus_virtual_document.find(
        syllabus_selected_section).string = openAI_response

    # 8. Write HTML
    write_html_history(syllabus_virtual_document,
                       openai_model, syllabus_selected_section)

    # Ask if word document should be written
    while True:
        if_write = input(
            f"\nWrite a word document of the updated syllabus?: \n1. Yes \n2. No \nR: ")

        if if_write == "1":
            write_docx(syllabus_virtual_document)
            print("\nDocument written")
            break

        if if_write == "2":
            break

    print("\n\n~~___Done___~~\n\n")
