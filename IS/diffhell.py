g = int(input("Enter g: "))
p = int(input("Enter p: "))
a = int(input("For user 1, a: "))
b = int(input("For user 2, b: "))
xa = (g**a) % p
xb = (g**b) % p
print("User1 will send Xa = ", xa, " to user2")
print("User2 will send Xb = ", xb, " to user1")
Ak = (xb**a) % p
Bk = (xa**b) % p
print("Ak is found to be ", Ak)
print("Bk is found to be ", Bk)
if Ak == Bk:
    print("Both can communicate further")
else:
    print("Communication cannot continue")
