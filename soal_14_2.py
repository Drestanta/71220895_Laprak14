import re
import random
import string
def password(n=8):
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(n)))
    return result_str
file = input("Masukkan file: ")
fhandle = open(file,"r")
for baris in fhandle:
    nama = re.split("@",baris)
    email = re.findall("\S+@\S+", baris)
    print(f"{email[0]} username: {nama[0]}, password: {password()}")
    