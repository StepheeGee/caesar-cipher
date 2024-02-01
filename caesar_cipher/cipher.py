# cipher.py
from caesar_cipher.corpus import english_words_set, english_names_set
import re, os, sys
import nltk
from nltk.corpus import words, names


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def load_english_words():
    english_words = set(words.words())
    return english_words


def encrypt(plain_text, shift):
    encrypted_text = ''
    for char in plain_text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    # print(f"Decrypting: {encrypted_text} with shift {shift}")
    return encrypt(encrypted_text, -shift)

def calculate_word_validity_ratio(decrypted_text, english_words_set):
    words = decrypted_text.split()
    valid_words = sum(word.lower() in english_words_set for word in words)
    return valid_words / len(words)

def crack(encrypted_text, english_words=english_words_set):
    for shift in range(26):
        decrypted_text = decrypt(encrypted_text, shift)
        validity_ratio = calculate_word_validity_ratio(decrypted_text, english_words)
        print(f"Shift {shift}: {decrypted_text}, Validity Ratio: {validity_ratio}")
        if validity_ratio > 0.8:
            return decrypted_text
    return ""


if __name__ == "__main__":
    english_words = load_english_words()

    # Example usage and tests
    print("Encrypt:", encrypt("What the hell is going on?", 6))
    print("Decrypt:", decrypt("Cngz znk nkrr oy muotm ut?", 6))
    print("Crack:", crack("Cngz znk nkrr oy muotm ut?"))

