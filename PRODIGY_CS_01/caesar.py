def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' for Encrypt or 'D' for Decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (number): "))
    except ValueError:
        print("Shift must be a valid integer.")
        return

    if choice == 'E':
        result = encrypt(message, shift)
        print(f"Encrypted Message: {result}")
    else:
        result = decrypt(message, shift)
        print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()
