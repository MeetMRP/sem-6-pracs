def encode(text: str) -> str:
    encoded_text = ''
    for t in text:
        encoded_text += chr(ord(t) + 3)
    return encoded_text

def decode(text: str) -> str:
    decoded_text = ''
    for t in text:
        decoded_text += chr(ord(t) - 3)
    return decoded_text

text = "meet patel"
encoded_text = encode(text)
decoded_text = decode(encoded_text)

print(f"Original: {text}")
print(f"Encoded: {encoded_text}")
print(f"Decoded: {decoded_text}")
