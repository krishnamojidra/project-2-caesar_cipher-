"""
DecodeLabs Industrial Training Kit
Project 2: Basic Encryption & Decryption (Caesar Cipher)

Goal:
    Implement a simple encryption and decryption technique.

Key Requirements:
    - Encrypt user text using a basic logic (Caesar cipher)
    - Decrypt the encrypted text
    - Display both encrypted and decrypted output

Author: (your name)
"""


def encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypts plaintext using the Caesar Cipher technique.

    Formula:  E_n(x) = (x + n) % 26

    Handles:
        - Uppercase letters
        - Lowercase letters
        - Spaces, numbers, punctuation (left unchanged)
    """
    result = []
    shift = shift % 26  # normalize shift so it always stays within 0-25

    for char in plaintext:
        if char.isupper():
            # A=65 ... Z=90
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(shifted))
        elif char.islower():
            # a=97 ... z=122
            shifted = (ord(char) - 97 + shift) % 26 + 97
            result.append(chr(shifted))
        else:
            # Edge case: spaces, digits, punctuation -> unchanged
            result.append(char)

    return "".join(result)


def decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypts ciphertext using the Caesar Cipher technique.

    Formula:  D_n(x) = (x - n) % 26

    Since Caesar Cipher is symmetric, decryption is simply
    encryption with the negative shift.
    """
    return encrypt(ciphertext, -shift)


def get_valid_shift():
    """Prompts the user for a valid integer shift key."""
    while True:
        try:
            shift = int(input("Enter shift key (e.g. 3): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("=" * 50)
    print(" DecodeLabs - Project 2: Basic Encryption & Decryption")
    print(" Technique Used: Caesar Cipher")
    print("=" * 50)

    # Step 1: Get user text
    plaintext = input("\nEnter the text you want to encrypt: ")

    # Step 2: Get shift key (custom key feature, as suggested in conclusion)
    shift = get_valid_shift()

    # Step 3: Encrypt
    encrypted_text = encrypt(plaintext, shift)

    # Step 4: Decrypt (to validate reversibility)
    decrypted_text = decrypt(encrypted_text, shift)

    # Step 5: Display results
    print("\n----- RESULTS -----")
    print(f"Original Text   : {plaintext}")
    print(f"Shift Key        : {shift}")
    print(f"Encrypted Text   : {encrypted_text}")
    print(f"Decrypted Text   : {decrypted_text}")

    # Step 6: Validation check
    if decrypted_text == plaintext:
        print("\n✅ Validation Passed: Decrypted text matches original input.")
    else:
        print("\n❌ Validation Failed: Mismatch detected.")


if __name__ == "__main__":
    main()
