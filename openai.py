
import openai

# Set OpenAI API key
openai.api_key = "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"

# Function to get openAI response


def call_openAI_API(prompt, model, text, section):

    print(
        f"\n______________\n\n Calling OpenAI with the prompt:\n -{prompt}- \n\n Using the model: '{model}' \n\n With the section: '{section}' \n\n______________\n\n Waiting for OpenAI response...\n")

    composedPrompt = f'{prompt} \n text: """{text}"""'

    # buenas prácticas para crear propmts
    # https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api

    if model == "edition":
        completions = openai.Edit.create(
            engine="text-davinci-edit-001",
            input=text,
            instruction=prompt,
            n=1,
            temperature=0.7,
        )

    if model == "completion":
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=composedPrompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

    # Get openAI response text
    response = completions.choices[0].text

    print(
        f'\n______________\n\nOpenAI responded with: \n\n {response}\n\n______________\n')

    return response
