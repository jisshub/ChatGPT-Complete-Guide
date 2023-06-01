def encode_text(text):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            if char == 'a':
                encoded_char = 'z'
            elif char == 'A':
                encoded_char = 'Z'
            else:
                encoded_char = chr(ord(char) - 1)
        else:
            encoded_char = char
        encoded_text += encoded_char
    return encoded_text

user_input = input("Enter the text to encode: ")
encoded_text = encode_text(user_input)
print("Encoded text:", encoded_text)


# python program to rename all file names in your directory

import os
def rename_files():
    # get file names from a folder
    file_list = os.listdir(r"C:\Users\Jom\Documents\MyPersonalWorks\chatgpt-complete-guide\files")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"C:\Users\Jom\Documents\MyPersonalWorks\chatgpt-complete-guide\files")
    # for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)


rename_files()
