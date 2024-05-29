# RSA ALGORITHM

## Generate keys
    **1**. Choose coprime p, q arbitrarily.
    **2**. Calculate n = p * q
    **3**. Calculate Ɵ(n) = (p-1) * (q-1)
    **4**. Choose a random number (e) coprime with Ɵ(n) and 1 < e < Ɵ(n)
    **5**. Find d where d * e is congruent to 1 when mod Ɵ(n)
        > [!TIP]
        > Use Extended Euclidean Algorithm to find d

==> Public Key (e, n)
==> Private Key (d, p, q)

## Encryption
    Assume M is message, M is encrypted by Public Key (e, n):
        ***(M ^ e) mod (n) = c***

## Decryption
    M is decrypted by Private Key (d, p, q):
        ***(c ^ d) mod (p*q) = M***

## Example
    **1**. p = 17, q = 23
    **2**. n = p * q = 391
    **3**. Ɵ(n) = (p-1) * (q-1) = 16 * 22 = 352
    **4**. Choose e = 13 (1 < 13 < 352, GCD(13, 352) = 1)
    **5**. d = 325, (13 * 325 mod 352 = 1)
==> Public key (13, 391)
==> Private key (325, 17, 23)

    Assume message: 24, message is encrypted by Public Key (e, n)
        ***(24 ^ 13) mod (391) = 346***
    
    message is decrypted by Private Key (d, p , q)
        ***(21 ^ 325) mod (391) = 24***

