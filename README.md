# pyXOR
A python implementation of XOR encryption

## Download and Install
1. Download python for your system. You should get it from the main website if you use Windows and system python will work well for Macs and *nix systems.
2. Clone this repo and use it normally.

## Usage
The program is incomplete as of now since it has no frontend (not even by CLI standards). However, if you are still interested in trying it out, you could always use python in the interactive mode and see how it works.

However to use the interactive mode you might have to actually read my code (which is well documented, I promise) but this is merely temporary.

## How it works
In order to use it (when it becomes useable), you need to enter the text you want to encrypt and a key. The output will be mumbo-jumbo. If you feed this mumbojumbo into the decryption function using the very same key. it should decrypt perfectly.

The way this works is by using the XOR function to XOR each and every byte in both the data and the key together. When you repeat the process except XOR the encoded text and the key, you should get the original text back.

If you are more daring, you could try double encryption, where the two parties use their own keys that they never disclose. This process is slightly tedious and maybe automated in a future version of this repo, but I'll describe it here nevertheless.

Person A encrypts their text with a key (key_A) and sends the message (encry_A) to Person B. Person B does not have key_A and therefore uses key_B to encrypt the already encrypted message from A to give encry_B and sends it back to A. A then decrypts encry_B using key_A and sends the new message decry_A to B. Finally, B decrypts decry_A using key_B and voila, you should get the original message back.

This process is still a little bit dodgy, so I would suggest sticking to single encryption for the time being.
