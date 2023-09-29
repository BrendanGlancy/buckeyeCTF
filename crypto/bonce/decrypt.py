# encrypted = output.txt
with open('output.txt', 'r') as f:
    encrypted = f.read().splitlines()

def decrypt(encrypted):
    decrypted = []
    for i in range(len(encrypted)):
        x = encrypted[i]
        if i < 10:
            nonce = str(i) * 28
        else:
            nonce = str(i) * 14
        decrypted.append(''.join(chr(int(a) ^ ord(b)) for a,b in zip(x.split(), nonce)))
    return decrypted

decrypted = decrypt(encrypted)
print(decrypted)
