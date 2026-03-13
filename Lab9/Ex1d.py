# Open the file name.txt and read its contents and print the number of names

with open("name.txt") as file_object:
    while (line := file_object.readline()):
        print(line.strip()) 
