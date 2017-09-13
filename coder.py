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


def encry(plaintext,key):
    # key must be in lowercase, or until I update the passkey function
    key = passkey(key.lower())
    
    # repeatin the key string to match with the length of the plaintext
    key = key*(len(plaintext)//len(key)) + key[:(len(plaintext)%len(key))]
    
    plain_bytes = list(map(ord,plaintext))
    key_bytes = list(map(ord,key))

    encoded_bytes = [ (p^k) for (p,k) in zip(plain_bytes,key_bytes) ]

    return "".join(list(map(chr,encoded_bytes)))


def decry(codetext,key):
    # even though the encry() and decry() functions do the same thing, 
    # I want to separate them for better clarity

    key = passkey(key.lower())
    
    key = key*(len(codetext)//len(key)) + key[:(len(codetext)%len(key))]
    
    code_bytes = list(map(ord,codetext))
    key_bytes = list(map(ord,key))

    decoded_bytes = [ (c^k) for (c,k) in zip(code_bytes,key_bytes) ]

    return "".join(list(map(chr,decoded_bytes))) 

# TODO : Frontend stuff
