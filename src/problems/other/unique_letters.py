def remove_duplicate(sentence):
    unique_chars = set()
    unique_sentence = []

    for char in sentence:
        if char not in unique_chars:
            unique_chars.add(char)
            unique_sentence.append(char)
        elif char == " ":
            unique_sentence.append(char)

    return "".join(unique_sentence)


if __name__ == '__main__':
    a = remove_duplicate("tree traversal algorithm")
    print(a)
