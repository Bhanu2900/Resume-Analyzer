from utils.skills_list import SKILLS


def extract_skills(tokens):
    extracted = set()

    # Match uni-grams (e.g. python, sql)
    for word in tokens:
        if word in SKILLS:
            extracted.add(word)

    # Match common bigrams (e.g. machine learning)
    for i in range(len(tokens) - 1):
        bigram = f"{tokens[i]} {tokens[i + 1]}"
        if bigram in SKILLS:
            extracted.add(bigram)

    return extracted
