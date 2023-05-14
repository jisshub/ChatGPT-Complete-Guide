import os

folder_path = input("Enter the folder path: ")

file_list = os.listdir(folder_path)

for file_name in file_list:
    if file_name.endswith(".jpg"):
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
