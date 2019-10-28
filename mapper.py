def letterToIndex(letter):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    idx = alphabet.find(letter)
    if idx == -1:       #means that it wasn't in the alphabet
        print("error:", letter, "is not in the alphabet")
    return idx