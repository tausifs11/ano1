import hashlib
txt1 = b'Tausif'
txt2 = b'Shaikh'
result = hashlib.md5(txt1)
result1 = hashlib.md5(txt2)
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())
print("The byte equivalent of hash is : ", end ="")
print(result1.digest())
