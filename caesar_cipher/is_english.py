# is_english.py

from caesar_cipher.corpus import english_words_set
import re

def count_words(text):
    word_count = 0
    candidate_words = text.split()

    for candidate in candidate_words:
        word = re.sub(r'[^a-zA-Z]', '', candidate)
        if word.lower() in english_words_set:
            print('english word: ' + word)
            word_count += 1
        else:
            print('not english word: ' + word)
            pass

    return word_count

count = count_words("Y'all gonna make me lose my mind.")
print('word_count: ' + str(count))
