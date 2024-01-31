# LAB - Class 18

## Project: Cryptography

## Author: Stephanie G. Johnson

## Date: 01-31-2024

### Overview

Cryptography is the practice and study of securing communication and data through the use of codes and ciphers. Its primary objective is to ensure the confidentiality, integrity, and authenticity of information. By employing various cryptographic techniques, plaintext data is transformed into ciphertext, making it unreadable to unauthorized individuals.

Cryptography plays a crucial role in information security, providing a foundation for secure communication, digital signatures, authentication mechanisms, and privacy protection. There are different types of cryptographic algorithms, including symmetric-key algorithms (using the same key for both encryption and decryption) and public-key algorithms (using a pair of keys, one for encryption and another for decryption).

In this project, we explore a classic encryption technique known as the Caesar Cipher. Named after Julius Caesar, this substitution cipher involves shifting each letter in the plaintext by a fixed number of positions down the alphabet. Understanding cryptography is essential for building secure systems and safeguarding sensitive information in various domains, including computer science, finance, and communication networks.

### Links and Resources

- [Cryptography](https://en.wikipedia.org/wiki/Cryptography)

- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

### Virtual Environment Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Install requests library: `pip install requests`


### How to Run

1. Activate the virtual environment (if not already activated).
2. Run `python caesar_cipher/cipher.py`

### Usage

- The `cipher.py` script provides functionality for encrypting, decrypting, and cracking messages using a Caesar Cipher.
- Adjust the `english_words.txt` file or provide your own corpus for cracking encrypted messages.
- Run tests using `pytest` to ensure the correctness of the implemented functions.

### Project Structure

- `caesar_cipher/cipher.py`: Contains the main implementation of the Caesar Cipher.
- `caesar_cipher/corpus.py`: Manages the English words corpus for cracking functionality.
- `tests/test_caesar.py`: Includes test cases for the implemented functions.
