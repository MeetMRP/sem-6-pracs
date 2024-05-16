import math
import hashlib

def sign_message(message_hash, d, n):    
    message_int = int.from_bytes(message_hash, byteorder='big')
    signature = pow(message_int, d, n)
    return signature

def verify_signature(signature, e, n):
    verified = pow(signature, e, n)
    return verified == signature

p, q = map(int, input("Enter prime numbers p and q: ").split())
n = p*q
phi = (p-1)*(q-1)
print("Value of phi is :",phi)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
print("Value of e :",e)

k = 1
while (1 + k * phi) % e != 0:
    k += 1
d = (1 + k * phi) // e
print("Value of d :",d)

message = input("Enter the message to sign: ")

message_bytes = message.encode()
md5_hash = hashlib.md5()
md5_hash.update(message_bytes)
message_hash = md5_hash.digest()

signature = sign_message(message_hash, d, n)
print("Signature:", signature)
verified = verify_signature(signature, e, n)
print("Signature verification:", verified)