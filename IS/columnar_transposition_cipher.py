def encode():
    order = sorted(range(k), key=lambda k:key[k])
    out_matrix = ['' for _ in range(k)]
    for i in range(k):
        for j in range(len(out_matrix)):
            out_matrix[j] += matrix[i][j]

    encoded_text = ''
    for i in order:
        encoded_text += out_matrix[i]

    return encoded_text


def decode():
    decoded_text = ''
    for i in range(k):
        decoded_text += ''.join(matrix[i])

    return decoded_text


plain_text = "my_name_is_meet"
plain_text_list = list(plain_text)
key = "mykey"
k = len(key)
matrix = [['' for _ in range(k)] for _ in range(k)]
for r in range(k):
    for c in range(k):
        matrix[r][c] = plain_text_list.pop(0) if plain_text_list else 'x'

print(matrix)

encoded_word = encode()
print("final encoded word: ", encoded_word)
print("decoded word: ", decode())