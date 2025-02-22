# Read and display the contents of a text file.
def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while accessing '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file("input.txt")
