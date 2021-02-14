def create_row():
    row = []
    for i in range(ord('A'), ord('Z')+1):
        row.append(chr(i))
    for i in range(ord('a'), ord('z')+1):
        row.append(chr(i))
    for i in range(ord('0'), ord('9') + 1):
        row.append(chr(i))
    row.append(' ')
    return row


def create_index_dict():
    index_map = {}
    index = 0
    for c in create_row():
        index_map[c] = index
        index += 1
    return index_map


def create_table():
    table = []
    row = create_row()
    length = len(row)
    for i in range(length):
        r = row[i:] + row[:i]
        table.append(r)
    return table


def encrypt(key_index_dict, table, key, text):
    cipher_text = []
    count = 0
    for t in text:
        k = key[count % len(key)]
        text_index = key_index_dict[t]
        key_index = key_index_dict[k]
        cipher_text.append(table[text_index][key_index])
        count += 1
    return "".join(cipher_text)


def decrypt(key_index_dict, table, key, cipher_text):
    text = []
    count = 0
    for c in cipher_text:
        k = key[count % len(key)]
        key_index = key_index_dict[k]
        row = table[key_index]
        cipher_index = 0
        for r in row:
            if r == c:
                break
            else:
                cipher_index += 1
        text.append(table[0][cipher_index])
        count += 1
    return "".join(text)


def main():
    key_index_dict = create_index_dict()
    table = create_table()

    while True:
        command = input("Enter e => encrypt, d => decrypt: ")
        key = input("Enter key: ")
        if command == 'e':
            text = input("Enter plain text: ")
            cipher_text = encrypt(key_index_dict, table, key, text)
            print("Cipher text: '" + cipher_text + "'")

        else:
            cipher_text = input("Enter cipher text: ")
            plain_text = decrypt(key_index_dict, table, key, cipher_text)
            print("Plain text: '" + plain_text + "'")


if __name__ == '__main__':
    main()
