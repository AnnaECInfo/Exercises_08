#  Exercise 1

def write_to_file(text, output_file_path):
    import os
    if os.path.exists(output_file_path):
        raise RuntimeError("Output file already exists!")
    else:
        with open(output_file_path, "w") as file:
            file.writelines(text)


#  Exercise 2

def count_stopwords(input_file_path):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r") as file:
        text = file.read()
    doc = nlp(text)
    stopword_list = 0
    for word in doc:
        if word.is_stop:
            stopword_list += 1
    return int(stopword_list)


#  Exercise 3

def remove_stopwords(input_file_path, output_file_path):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r") as f1:
        text = f1.read()
    doc = nlp(text)
    output_text = ""
    for word in doc:
        if not word.is_stop:
            output_text += word.text + " "
            with open(output_file_path, "a") as f2:
                f2.write(output_text)


#  Exercise 4

def tokenize_text(input_file_path, output_file_path):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r") as f1:
        text = f1.read()
        doc = nlp(text)
    with open(output_file_path, "w") as f2:
        for token in doc:
            f2.writelines(f"{token.text: {10}}{token.pos_:{10}}{token.dep_:{10}}")


#  Exercise 5

def save_visualization(input_file_path, output_file_path):
    import spacy
    from spacy import displacy
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r") as f1:
        text = f1.read()
        doc = nlp(text)
        svg = displacy.render(doc, style="dep")
    with open(output_file_path, "w") as f2:
        f2.write(svg)
