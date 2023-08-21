def encrypt(data: str, shift: int):
    data_encoded = data.encode('utf-8')
    data_barray = bytearray(data_encoded)
    data_encrypted = data_barray.copy()

    for i in range(len(data_encrypted)):
        data_encrypted[i] += shift

    return data_encrypted.decode('utf-8')


def decrypt(data: str, shift: int):
    data_decoded = data.encode('utf-8')
    data_barray = bytearray(data_decoded)
    data_decrypted = data_barray.copy()

    for i in range(len(data_decrypted)):
        data_decrypted[i] -= shift

    return data_decrypted.decode('utf-8')


key = 3
message = input("Type something: ")
encoded = encrypt(message, key)
decoded = decrypt(encoded, key)

print(f"Encrypted message: {encoded}")
print(f"Decrypted message: {decoded}")
