import rsa
import time 
import os


with open("public.pem", "rb") as f:
    pubKey = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    privKey = rsa.PrivateKey.load_pkcs1(f.read())


os.makedirs("encryption", exist_ok=True)

encTimes = []
num = [50*i for i in range(11)]

for i in num:
    fileName = "text/" + str(i)
    with open(fileName, "rb") as f:
        msg = f.read()
        fileName2 = "encryption/" + str(i)

        with open(fileName2, "wb") as f2:
            s = time.time()
            msg_enc = rsa.encrypt(msg, pubKey)
            e = time.time()

            encTimes.append((e - s))

            f2.write(msg_enc)

print(encTimes)


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.plot(num, encTimes)
ax.set(xlabel='Character', ylabel='Time (ms)',
       title='Encryption Time Plot')
ax.grid()
plt.show()