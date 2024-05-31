import rsa
import time 

start_time = time.time()
(pubKey, privKey) = rsa.newkeys(4096)
end_time = time.time()
total_time = end_time - start_time
print(f"Generate Key: {total_time:.4f}s")


### Save public key and private key into pem file.
with open("public.pem", "wb") as f:
    key = pubKey._save_pkcs1_pem()
    f.write(key)

with open("private.pem", "wb") as f:
    key = privKey._save_pkcs1_pem()
    f.write(key)
#########################
