import math 

p, q = map(int, input("Enter prime numbers p and q : ").split())
n = p*q
phi = (p-1)*(q-1)
print("Value of phi is :",phi)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
print("Value of e : ",e)

k = 1
while (1 + k * phi) % e != 0:
    k += 1
d = (1 + k * phi) // e
print("Value of d :",d)

pt = int(input("Enter plain text : "))
ct = (pt**e) % n
print("Encrypted Text :",ct)
decryptedText = (ct**d) % n
print("Decrypted Text :",decryptedText)