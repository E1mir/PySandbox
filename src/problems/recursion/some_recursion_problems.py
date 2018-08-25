def rec_sum(n):
    if n == 0:
        return 0

    return n + rec_sum(n - 1)


def sum_func(n):
    if n < 10:
        return n

    return n % 10 + sum_func(n // 10)


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output


if __name__ == '__main__':
    print(rec_sum(10))

    print(sum_func(1115555))

    print(word_split('themanran', ['the', 'ran', 'man']))
    print(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
    print(word_split('themanran', ['clown', 'ran', 'man']))
