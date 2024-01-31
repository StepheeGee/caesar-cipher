# cipher.py

from .corpus import english_words_set, english_names_set
import re


def load_english_words(file_path):
    with open(file_path, 'r') as file:
        words = set(word.strip().lower() for word in file)
    return words

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
    return encrypt(encrypted_text, -shift)

def crack(encrypted_text, english_words=english_words_set):
    for shift in range(26):
        decrypted_text = decrypt(encrypted_text, shift)
        words = decrypted_text.split()
        valid_words = sum(word.lower() in english_words for word in words)
        if valid_words / len(words) > 0.8:
            return decrypted_text
    return ""

if __name__ == "__main__":
    english_words = load_english_words('english_words.txt')

