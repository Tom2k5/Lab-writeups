---
tags:
  - "#cryptography"
  - "#xor"
---

### Source Code - Server

```python
import random
import socketserver 
import socket, os
import string

flag = open('flag.txt','r').read().strip()

def send_message(server, message):
    enc = message.encode()
    server.send(enc)

def setup(server, key):
    flag = 'THM{thisisafakeflag}' 
    xored = ""

    for i in range(0,len(flag)):
        xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))

    hex_encoded = xored.encode().hex()
    return hex_encoded

def start(server):
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    key = str(res)
    hex_encoded = setup(server, key)
    send_message(server, "This XOR encoded text has flag 1: " + hex_encoded + "\n")
    
    send_message(server,"What is the encryption key? ")
    key_answer = server.recv(4096).decode().strip()

    try:
        if key_answer == key:
            send_message(server, "Congrats! That is the correct key! Here is flag 2: " + flag + "\n")
            server.close()
        else:
            send_message(server, 'Close but no cigar' + "\n")
            server.close()
    except:
        send_message(server, "Something went wrong. Please try again. :)\n")
        server.close()

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler)
    server.serve_forever()
```

### Key - Flag Decryptor
- `hex_encoded` has 40 bytes.
- Every 5 bytes of `hex_encoded` must be decrypted by XOR with flag to get the key.
- The given flag is fake, but the truth we got `THM{` as first four components of key.
- The last component is xorring with the last byte of `hex_encoded` -> `}` because of fake material in the middle of given flag.

```python
from pwn import xor

flag = 'THM{thisisafakeflag}'
hex_encoded = "15263b1547700f1a00430416022f43355a1505540000045d562d220f0662331a0f5e423316391c4a"
xored_bytes = bytes.fromhex(hex_encoded)
key = xor(xored_bytes[:4], b'THM{') + xor(xored_bytes[-1], b'}')
print(key)
print(xor(xored_bytes, key.encode())
```