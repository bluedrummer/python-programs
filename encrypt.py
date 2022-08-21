#Hello thank you for using my program
#This works with Python3
#What does this program do?: This program turns text into ciphertext or ciphertext into text with a password
#Thank you for using!
import base64

ciphertext = ""
encode_decode = ""

print("Encode or decode text (encode/decode)? ")
print()
while True:
    encode_decode = input()
    if encode_decode.upper() == "ENCODE" or encode_decode.upper() == "DECODE":
        break
    print("Enter Encode Or Decode")
    print()

if encode_decode.upper() == "ENCODE":
    print()
    print("Enter clear text to encode: ")
    text = input()
    print()

if encode_decode.upper() == "DECODE":
    print()
    print("Enter ciphertext in base64 to decode: ")
    text = input()
    text = base64.b64decode(text).decode()
#    print(type(text))
    print()

print("Enter your one-time-password")
pad = input()
#pad = base64.b64decode(pad.encode("ascii"))

i = 0
key_length = len(pad)

for t in text:
    key_index = i % key_length
#    print(type(t))
    a = int.from_bytes(bytes(t.encode("ascii")),"big")
    b = int.from_bytes(bytes(pad[key_index].encode("ascii")),"big")
    c = a ^ b
    ciphertext += chr(c)
    i += 1

print()
if encode_decode.upper() == "ENCODE":
    print("Here is your encoded ciphertext")
    print(base64.b64encode(ciphertext.encode("ascii")))

if encode_decode.upper() == "DECODE":
    print("Here is your decoded text")
    print(ciphertext)
