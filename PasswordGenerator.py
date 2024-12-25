import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using the characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for password length
password_length = int(input("Enter the desired password length: "))

# Generate the password
generated_password = generate_password(password_length)

# Display the generated password
print("Generated Password:", generated_password)
