def num2str(number):
    """Convert a number to a string with 4 decimal places."""
    return str(round(number, 4))

def tokenize(text):
    return text.replace(".","").replace(",","").lower().split()

def vec2str(vector):
    return "[" + ', '.join(map(num2str, vector)) + "]"