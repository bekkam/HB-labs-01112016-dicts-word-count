def count_words(file_name):
    """Counts words in a txt file"""

    word_log = open(file_name)

    word_occurance = {}

    for line in word_log:
        line = line.rstrip()
        words = line.split()

        for word in words:
            word = word.lower()
            if not word.isalpha():
                word = word[:-1]
            quantity = word_occurance.get(word, 0)
            word_occurance[word] = quantity + 1

    print word_occurance.items()


count_words("test.txt")
