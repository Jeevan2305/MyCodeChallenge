# Handle exceptions for file not found.
def file_available(filename):
    try:
        with open(filename, 'r') as f:
            return "File exist"
    except FileNotFoundError:
        return "File does not exist"

print(file_available("input.txt"))
