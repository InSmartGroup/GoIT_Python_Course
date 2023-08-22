def encrypt(text, shift=None):
    coded_text = ""
    text_b = bytearray(text.encode('utf-8'))

    for i in range(len(text_b)):
        n = text_b[i] + shift

        if n > 255:
            n -= 255

        text_b[i] = n
        coded_text += chr(text_b[i])

    return text_b, coded_text


def decrypt(text_bytes, shift):
    decoded_text = ""

    for i in range(len(text_bytes)):
        n = text_bytes[i] - shift

        if n < 0:
            n += 255

        text_bytes[i] = n
        decoded_text += chr(text_bytes[i])

    return text_bytes, decoded_text


to_encrypt = input("Type something: ")
key = 33

coded_bytes, coded = encrypt(to_encrypt, key)
decoded_bytes, decoded = decrypt(coded_bytes, key)

print(f"Encrypted message: {coded}")
print(f"Decrypted message: {decoded}")
