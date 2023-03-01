# Posible refactorización: crear una única función que reciba una lista de posibles opciones de input, 
# iterar sobre esta para imprimir las opciones y devolver el valor seleccionado

def capture_openAI_model(): 
    while True:
        get_model_promp = input("\nWich AI model describes better what you want to do with the text?: \n1. Edition \n2. Completion \nR: ")

        # Romper el ciclo imprimiendo la opcion seleccionada y retornando dicha selección en minúscula
        def break_loop(model_name):
                print(f"\n{model_name} selected")
                return model_name.lower()

        if get_model_promp == "1":
            return break_loop("Edition")

        if get_model_promp == "2":
            return break_loop("Completion")

        print("\nType a valid option and press ENTER")

def capture_syllabus_selected_section():

    while True:
        # Prompt para seleccionar la sección a usar
        get_section_prompt = input(
            "\nWich section of the document you wish to use?: \n1. Objective \n2. Justification \nR: ")

        # Romper el ciclo imprimiendo la opcion seleccionada y retornando dicha selección en minúscula
        def break_loop(section_name):
            print(f"\n{section_name} selected:")
            return section_name.lower()

        if get_section_prompt == "1":
            return break_loop("Objective")

        if get_section_prompt == "2":
            return break_loop("Justification")

        print("\nType a valid option and press ENTER")