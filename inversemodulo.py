def extended_euclid(a, b):
  # Base case: if b is 0, then a is the gcd and its inverse (mod a) is 1
  if b == 0:
    return a, 1, 0
  
  # Recursively find gcd(b, a % b) and update coefficients (s1, t1)
  (d, s1, t1) = extended_euclid(b, a % b)
  
  # Calculate coefficients (s, t) for original equation (a, b)
  s = t1
  t = s1 - (a // b) * t1
  
  # Return the gcd (d) and coefficients (s, t)
  return d, s, t

def mod_inverse(a, m):
  # Check if a has an inverse (coprime with m)
  d, s, _ = extended_euclid(a, m)
  if d != 1:
    return "Modular inverse does not exist"
  
  # Since a and m are coprime, s is the inverse modulo m (might be negative)
  # Adjust negativity by adding m (uses modular arithmetic property)
  return (s + m) % m 

print (mod_inverse(13, 352))
print (346**325 % 391)