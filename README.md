# LAB - Class 18

## Project: Cryptography

## Author: Stephanie G. Johnson

## Date: 01-31-2024

### Overview

Cryptography is the practice and study of securing communication and data through the use of codes and ciphers. Its primary objective is to ensure the confidentiality, integrity, and authenticity of information. By employing various cryptographic techniques, plaintext data is transformed into ciphertext, making it unreadable to unauthorized individuals.

Cryptography plays a crucial role in information security. It is used to protect sensitive information, such as bank accounts, credit cards, and passwords, from unauthorized access.

In this project, we explore a classic encryption technique known as the Caesar Cipher. Named after Julius Caesar, this substitution cipher involves shifting each letter in the plaintext by a fixed number of positions down the alphabet. Understanding cryptography is essential for building secure systems and safeguarding sensitive information in various domains, including computer science, finance, and communication networks.

### Links and Resources

- [Cryptography](https://en.wikipedia.org/wiki/Cryptography)

- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

- [NLTK Documentation](https://www.nltk.org/)

- [NLTK Corpus](https://www.nltk.org/nltk_data/)

### Virtual Environment Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`


### How to Run

1. Activate the virtual environment (if not already activated).
2. Run from the parent directory: `python3 -m caesar_cipher.cipher`


### Usage

#### Encrypting, Decrypting, and Cracking Messages

1. The `cipher.py` script allows you to perform various operations using a Caesar Cipher.

    - **Encrypt a Message:**
      ```bash
      python3 -m caesar_cipher.cipher encrypt "Your message here" 3
      ```
      Replace `"Your message here"` with the message you want to encrypt and `3` with the desired shift value.

    - **Decrypt a Message:**
      ```bash
      python3 -m caesar_cipher.cipher decrypt "Encrypted message here" 3
      ```
      Replace `"Encrypted message here"` with the message you want to decrypt and `3` with the correct shift value.

    - **Crack an Encrypted Message:**
      ```bash
      python3 -m caesar_cipher.cipher crack "Encrypted message here"
      ```
      Replace `"Encrypted message here"` with the encrypted message you want to crack.

2. Run tests using `pytest` to ensure the correctness of the implemented functions.
   ```bash
   pytest
   ```

### Project Structure

- `caesar_cipher/cipher.py`: Contains the main implementation of the Caesar Cipher.
- `caesar_cipher/corpus.py`: Manages the English words corpus for cracking functionality.
- `caesar_cipher/is_english.py`: Provides functions for checking English word validity.
- `tests/test_caesar.py`: Includes test cases for the implemented functions.

