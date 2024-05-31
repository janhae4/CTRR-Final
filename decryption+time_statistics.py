import rsa
import time 
import os


with open("public.pem", "rb") as f:
    pubKey = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    privKey = rsa.PrivateKey.load_pkcs1(f.read())


os.makedirs("decryption", exist_ok=True)

decTimes = []
num = [50*i for i in range(11)]

for i in num:
    fileName = "encryption/" + str(i)
    with open(fileName, "rb") as f:
        msg = f.read()
        fileName2 = "decryption/" + str(i)

        with open(fileName2, "wb") as f2:
            s = time.time()
            msg_dec = rsa.decrypt(msg, privKey)
            e = time.time()

            decTimes.append((e - s))

            f2.write(msg_dec)

print(decTimes)


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(num, decTimes)
ax.set(xlabel='Character', ylabel='Time (ms)',
       title='Encryption Time Plot')
ax.grid()
plt.show()
