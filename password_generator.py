import random
import string
def generate_password(length):
    """A random password is generated"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password


if __name__ == "__main__":
    length = int(input("Enter the number of characters: "))
    password = generate_password(length)
    print("A password has been generated:")
    print(password)