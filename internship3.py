import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords=1, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def print_generated_passwords(passwords):
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

def main():
    try:
        length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    passwords = generate_multiple_passwords(num_passwords, length)

    print_generated_passwords(passwords)

if __name__ == "__main__":
    main()

