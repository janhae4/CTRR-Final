import random
import string
import os

os.makedirs("text", exist_ok=True)

    
def generate(filename, size):
    f = "text/" + filename
    with open(f, "wb") as f:
        msg = ""
        for _ in range(size):
            msg += random.choice(string.ascii_letters)
        f.write(msg.encode('utf-8'))

num = [50*i for i in range(11)]
print(num)
for i in num:
    generate(str(i), i)

