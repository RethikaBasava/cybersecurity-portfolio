
import secrets
import string


def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("===== Python Password Generator =====")

    try:
        length = int(input("Enter password length (minimum 8): "))

        password = generate_password(length)

        print("Generated password:", password)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
