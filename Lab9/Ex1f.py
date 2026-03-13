# Open the file name.txt and read its contents and print the number of names
# Apend a new name at the end of the file 

with open("name.txt") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)
    print(f"number of names: {len(contents_list)}")

with open("name.txt", "a") as file_object:
    print("Appending new name to the end of the file...")
    file_object.write("Adam, Amy\n")
    contents_list.append("Adam, Amy\n")
    print(f"number of names after appending: {len(contents_list)}")