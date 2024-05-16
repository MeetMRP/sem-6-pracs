def vernom(text: str) -> str:
    encoded_text = ''
    for i in range(len(text)):
        x = ord(text[i]) - ord('a')
        y = ord(key[i]) - ord('a')
        z = (x^y)%26
        encoded_text += chr(z + ord('a'))
    return encoded_text


text = "meetpatel"
key = "abcdefghi"
encoded_text = vernom(text)
decoded_text = vernom(encoded_text)

print(f"Original: {text}")
print(f"Encoded: {encoded_text}")
print(f"Decoded: {decoded_text}")
