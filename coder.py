#! python3

# This is an encrypting program that uses XOR to encrypt. The cool thing is,
# since XOR operations repeat the results when used repeatedly, we can use
# it as a method to encrypt-decrypt data.


def passkey(word):
    # this function removes all the repeating characters
    # key thing to note - `word` is ALL LOWER CASE
    password = ""

    for i in word:
        if not i in password:
            password+=i
    
    return password


def crypt(text,key):
    # this function does both the decoding and encoding
    # key must be in lowercase, or until I update the passkey function
    key = passkey(key.lower())
    
    # repeatin the key string to match with the length of the plaintext
    key = key*(len(text)//len(key)) + key[:(len(text)%len(key))]
    
    text_bytes = list(map(ord,text))
    key_bytes = list(map(ord,key))

    coded_bytes = [ (t^k) for (t,k) in zip(text_bytes,key_bytes) ]

    return "".join(list(map(chr,coded_bytes)))

# TODO : Frontend stuff

