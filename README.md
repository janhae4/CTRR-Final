# RSA ALGORITHM

## Generate keys
**1**. Choose coprime p, q arbitrarily.<br>
**2**. Calculate n = p * q<br>
**3**. Calculate Ɵ(n) = (p-1) * (q-1)<br>
**4**. Choose a random number (e) coprime with Ɵ(n) and 1 < e < Ɵ(n)<br>
**5**. Find d where d * e is congruent to 1 when mod Ɵ(n)<br>
> [!TIP]
> Use Extended Euclidean Algorithm to find d
 
> Public Key (e, n)<br>
> Private Key (d, p, q)<br>

## Encryption
Assume M is message, M is encrypted by Public Key (e, n):<br>
>***(M ^ e) mod (n) = c***

## Decryption
M is decrypted by Private Key (d, p, q):<br>
>***(c ^ d) mod (p*q) = M***<br>

## Example
**1**. p = 17, q = 23<br>
**2**. n = p * q = 391<br>
**3**. Ɵ(n) = (p-1) * (q-1) = 16 * 22 = 352<br>
**4**. Choose e = 13 (1 < 13 < 352, GCD(13, 352) = 1)<br>
**5**. d = 325, (13 * 325 mod 352 = 1)<br>
> Public key (13, 391)<br>
> Private key (325, 17, 23)<br>

Assume message: 24, message is encrypted by Public Key (e, n)<br>
>***(24 ^ 13) mod (391) = 346***<br>
    
Message is decrypted by Private Key (d, p , q)<br>
>***(21 ^ 325) mod (391) = 24***<br>

