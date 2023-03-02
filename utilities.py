# Given a string, trims it to a given length

def trim_text(text, length):
    preprocess_text = text.replace("\n", " ")
    trims = [(preprocess_text[i:i + length])
             for i in range(0, len(text), length)]
    return trims[0]