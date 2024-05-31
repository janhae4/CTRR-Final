import os
import time
import rsa
import random
import string
import matplotlib.pyplot as plt


###GENERATE TESTCASE
def generate(filename, size):
    f = "text/" + filename
    with open(f, "wb") as f:
        msg = ''.join(random.choice(string.ascii_letters) for _ in range(size))
        f.write(msg.encode('utf-8'))

def generate_test_case():
    os.makedirs("text", exist_ok=True)
    num = [50*i for i in range(11)]
    for i in num:
        generate(str(i), i)


###GENERATE KEY
def generate_key():
    start_time = time.perf_counter()
    (PUBKEY, PRIVKEY) = rsa.newkeys(4096)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Generate Key: {total_time:.4f}s")
    with open("public.pem", "wb") as f:
        key = PUBKEY._save_pkcs1_pem()
        f.write(key)

    with open("private.pem", "wb") as f:
        key = PRIVKEY._save_pkcs1_pem()
        f.write(key)



### LOAD PUBLIC KEY AND PRIVATE KEY FROM PEM FILE
def load_keys():
    with open("public.pem", "rb") as f:
        PUBKEY = rsa.PublicKey.load_pkcs1(f.read())
    with open("private.pem", "rb") as f:
        PRIVKEY = rsa.PrivateKey.load_pkcs1(f.read())
    return PUBKEY, PRIVKEY


### ENCRYPTION TEST CASE
def encryption():
    os.makedirs("encryption", exist_ok=True)
    PUBKEY, _ = load_keys()
    ENCTIMES = []
    num = [50*i for i in range(11)]

    for i in num:
        with open(f"text/{i}", "rb") as f:
            msg = f.read()
            with open(f"encryption/{i}", "wb") as f2:
                s = time.perf_counter()
                msg_enc = rsa.encrypt(msg, PUBKEY)
                e = time.perf_counter()
                total = (e - s)*1000
                print(f"Time to encryption: {total}ms")
                ENCTIMES.append(total)
                f2.write(msg_enc)
    return ENCTIMES

#### PLOT ENCRYPTION TIME
def plot_time(encTimes, decTimes):
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle("Time of encryption and decryption")
    num = [50*i for i in range(11)]
    ax1.plot(num, encTimes)
    ax2.plot(num, decTimes)
    ax2.set_xlabel('Character Count')
    ax1.set_ylabel('Ecryption Time (ms)')
    ax2.set_ylabel('Decryption Time (ms)')
    ax1.grid()
    ax2.grid()
    plt.show()



### DECRYPTION TEST CASE
def decryption():
    os.makedirs("decryption", exist_ok=True)
    _, PRIVKEY = load_keys()
    DECTIMES = []
    num = [50*i for i in range(11)]

    for i in num:
        with open(f"encryption/{i}", "rb") as f:
            msg = f.read()
            with open(f"decryption/{i}", "wb") as f2:
                s = time.perf_counter()
                msg_dec = rsa.decrypt(msg, PRIVKEY)
                e = time.perf_counter()
                total = (e - s)*1000
                print(f"Time to decryption: {total}ms")
                DECTIMES.append(total)
                f2.write(msg_dec)
    return DECTIMES



def main():
    generate_key()
    generate_test_case()
    TIME1 = encryption()
    TIME2 = decryption()
    plot_time(TIME1, TIME2)

if __name__ == "__main__":
    main()





