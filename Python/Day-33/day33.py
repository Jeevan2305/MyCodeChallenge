# Write data to a text file.
def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data + "\n")
    
d = input("Enter data to write : ")
write_data_to_file(d, "data.txt")
