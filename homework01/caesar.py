import typing as tp


def encrypt_caesar(plaintext, shift=3):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    
    ciphertext = ''
    for i in plaintext:
        if (ord("z") >= ord(i) >= ord("a")):
            ciphertext += chr(ord('a') + (ord(i) + shift - ord("a")) % 26)
        elif (ord("Z") >= ord(i) >= ord("A")):
            ciphertext += chr(ord('A') + (ord(i) + shift - ord("A")) % 26)
        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext, shift=3):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    plaintext = encrypt_caesar(ciphertext, -shift)
    return plaintext



def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    text = ''
    # PUT YOUR CODE HERE
    while text not in dictionary:
        best_shift += 1
        text = encrypt_caesar(ciphertext, best_shift)
    return best_shift
