import caesar

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    index = 0
    for i in plaintext:
        if (index >= len(keyword)):
            index = 0   
        if ("a" <= i <= "z"):
            ciphertext += caesar.encrypt_caesar(i, ord(keyword[index].lower()) - ord("a"))
        elif ("A" <= i <= "Z"):
            ciphertext += caesar.encrypt_caesar(i, ord(keyword[index].upper()) - ord("A"))
        else:
            ciphertext += i
        index += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    index = 0
    for i in ciphertext:
        if (index >= len(keyword)):
            index = 0   
        if ("a" <= i <= "z"):
            plaintext += caesar.decrypt_caesar(i, ord(keyword[index].lower()) - ord("a"))
        elif ("A" <= i <= "Z"):
            plaintext += caesar.decrypt_caesar(i, ord(keyword[index].upper()) - ord("A"))
        else:
            plaintext += i
        index += 1
    return plaintext
