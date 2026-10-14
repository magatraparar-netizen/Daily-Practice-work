def write_file(filename , text):
    with open(filename , 'w') as file:
        file.write(text)
    print("file written successfully!")

def read_file(filename):
    with open(filename , 'r') as file:
        return file.read()
