# Calculate the average of numbers in a text file.
def average_numbers_in_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file]
            return sum(numbers) / len(numbers)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except ValueError:
        print(f"The file {filename} contains non-numeric data")
        return None
    
print(average_numbers_in_file("input.txt"))
