First file 

def validate_input(user_input):
    """Check if input is not empty and is a string."""
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    return False


def convert_to_binary(text):
    """Convert a string or number to binary representation."""
    if text.isdigit():
        # For age (number)
        return bin(int(text))
    else:
        # For name (text)
        return ' '.join(format(ord(char), '08b') for char in text)


def create_message(name, age, name_binary, age_binary):
    """Create a personalized message including binary values."""
    message = (
        f"Hello {name}, you are {age} years old!\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
    return message
