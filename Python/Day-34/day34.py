# Append data to an existing text file.
def append_data_to_file(data, filename):
    with open(filename, 'a') as file:
        file.write(data + "\n")
    
d = input("Enter data to write : ")
append_data_to_file(d, "data.txt")
