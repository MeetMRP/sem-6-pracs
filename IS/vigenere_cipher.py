key = 'hiii'
plain_text = 'meet'

if len(key) != len(plain_text):
    print('size not matched')

key_list = list(key)
n = len(key)


def encode(plain_text):
    encoded_text = ''
    for i in range(len(plain_text)):
        char = chr(
            ((ord(plain_text[i]) - ord('a') + ord(key[i]) - ord('a')) % 26) + ord('a'))
        encoded_text += char
    return encoded_text


def decode(text):
    decoded_text = ''
    for i in range(n):
        word = chr(
            (((ord(text[i]) - ord('a')) - (ord(key[i]) - ord('a'))) % 26) + ord('a'))
        decoded_text += word

    return decoded_text


encoded_word = encode(plain_text=plain_text)
print("final encoded word: ", encoded_word)
print("decoded word: ", decode(encoded_word))
