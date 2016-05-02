from pycipher import Enigma

plaintext = "MygrandfatherwasnotBretonbuthewasreallycool".upper()
ciphertext = Enigma(
    settings=('A', 'A', 'A'),
    rotors=(3, 2, 1),
    reflector='B',
    ringstellung=('A', 'A', 'A'),
    steckers=[('G', 'A'), ('M', 'E'), ('F', 'N'), ('Y', 'J'), ('S', 'O'),
              ('P', 'C'), ('V', 'D'), ('K', 'I'), ('X', 'H'), ('W', 'Z')]
    ).encipher(plaintext)

plaintext_recover = Enigma(
    settings=('A', 'A', 'A'),
    rotors=(3, 2, 1),
    reflector='B',
    ringstellung=('A', 'A', 'A'),
    steckers=[('G', 'A'), ('M', 'E'), ('F', 'N'), ('Y', 'J'), ('S', 'O'),
              ('P', 'C'), ('V', 'D'), ('K', 'I'), ('X', 'H'), ('W', 'Z')]
    ).encipher(ciphertext)

print("[+] Plaintext : %s" % plaintext)
print("[+] Ciphertext : %s" % ciphertext)
print("[+] Plaintext recovered : %s" % plaintext_recover)
