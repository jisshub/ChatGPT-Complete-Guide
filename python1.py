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
