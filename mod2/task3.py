import sys

def decrypt(message: str) -> str:
    decrypt_message = ''
    symbol_ind = 0
    start_point_ind = -1
    while symbol_ind < len(message):
        if message[symbol_ind] != '.':
            decrypt_message += message[symbol_ind]
            symbol_ind += 1
            start_point_ind = -1
        else:
            if start_point_ind < 0:
                start_point_ind = symbol_ind
                symbol_ind += 1
            else:
                count = (symbol_ind - start_point_ind + 1)//2
                decrypt_message = decrypt_message[:len(decrypt_message) - count]
                symbol_ind += 1
                start_point_ind = -1
    return decrypt_message.replace('.', '')

if __name__ == '__main__':
    print(decrypt(sys.stdin.read()))