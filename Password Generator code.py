import random
import string

def generate_password(length, complexity):
    if complexity == "Easy":
        chars = string.ascii_letters + string.digits
    elif complexity == "Medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "Hard":
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = "".join(random.choice(chars) for i in range(length))

    return password
