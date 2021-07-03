import hashlib
text = input("Enter Your Name:")
hash_object = hashlib. md5(text. encode())
md5_hash = hash_object. hexdigest() 
print("Your Name In MD5 :",md5_hash)