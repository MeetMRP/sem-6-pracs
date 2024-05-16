import string


def find_matrix_index(character) -> tuple:
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == character:
                return (r, c)
    return (-1, -1)


def encode(plain_text: str) -> str:
    plain_text_list = list(plain_text)
    encoded_text = ''
    while plain_text_list:
        T1 = plain_text_list.pop(0)
        T2 = plain_text_list.pop(0) if plain_text_list else 'x'

        T1_row, T1_col = find_matrix_index(character=T1)
        T2_row, T2_col = find_matrix_index(character=T2)

        if T1_row == T2_row:
            word = matrix[T1_row][(T1_col+1) % 5] + \
                matrix[T2_row][(T2_col+1) % 5]
        elif T1_col == T2_col:
            word = matrix[(T1_row+1) % 5][T1_col] + \
                matrix[(T2_row+1) % 5][T2_col]
        else:
            word = matrix[T1_row][T2_col] + matrix[T2_row][T1_col]

        print(f'{T1+T2} -> {word}')
        encoded_text += word

    return encoded_text


def decode(plain_text: str) -> str:
    plain_text_list = list(plain_text)
    encoded_text = ''
    while plain_text_list:
        T1 = plain_text_list.pop(0)
        T2 = plain_text_list.pop(0) if plain_text_list else 'x'

        T1_row, T1_col = find_matrix_index(character=T1)
        T2_row, T2_col = find_matrix_index(character=T2)

        if T1_row == T2_row:
            word = matrix[T1_row][(T1_col-1) % 5] + \
                matrix[T2_row][(T2_col-1) % 5]
        elif T1_col == T2_col:
            word = matrix[(T1_row-1) % 5][T1_col] + \
                matrix[(T2_row-1) % 5][T2_col]
        else:
            word = matrix[T1_row][T2_col] + matrix[T2_row][T1_col]

        print(f'{T1+T2} -> {word}')
        encoded_text += word

    return encoded_text


alphabets = list(string.ascii_lowercase)
alphabets.remove('j')

key = 'monarchy'
key_list = [k for k in key]
plain_text = 'instruments'

matrix = [[0 for _ in range(5)] for _ in range(5)]
for r in range(5):
    for c in range(5):
        if key_list:
            character = key_list.pop(0)
            matrix[r][c] = character
            if character in alphabets:
                alphabets.remove(character)
        else:
            matrix[r][c] = alphabets.pop(0)
print("matrix: ", matrix)

encoded_word = encode(plain_text=plain_text)
print("final encoded word: ", encoded_word)
print("decoded word: ", decode(encoded_word))
