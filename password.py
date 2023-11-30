import secrets
import string

def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    # Define character sets
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    # Generate password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for password length and count
    try:
        length = int(input("Enter the length of the password: "))
        count = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Get user preferences for character types
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and print passwords
    for _ in range(count):
        password = generate_password(length, uppercase, digits, special_chars)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
