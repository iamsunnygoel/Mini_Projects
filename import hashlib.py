import hashlib

def hash_phone(phone):
    num = phone.strip()
    h = hashlib.sha256(num.encode('utf-8')).hexdigest()
    return h

print("This is your Hash id--->",hash_phone("+918447929916"))



