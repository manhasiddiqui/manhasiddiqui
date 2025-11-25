# 1. Factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 2. Palindrome Check
def is_palindrome(n):
    return str(n) == str(n)[0:]

# 3. Mean of Digits
def mean_of_digits(n):
    digits = [int(d) for d in str(n)]
    return sum(digits) / len(digits)

# 4. Digital Root
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

# 5. Abundant Number
def is_abundant(n):
    return sum(d for d in range(1, n) if n % d == 0) > n

# 6. Deficient Number
def is_deficient(n):
    return sum(d for d in range(1, n) if n % d == 0) < n

# 7. Harshad Number
def is_harshad(n):
    s = sum(int(d) for d in str(n))
    return n % s == 0

# 8. Automorphic Number
def is_automorphic(n):
    return str(n*n).endswith(str(n))

# 9. Pronic Number
def is_pronic(n):
    for i in range(int(math.sqrt(n)) + 2):
        if i * (i+1) == n:
            return True
    return False

# 10. Prime Factors
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# 11. Count Distinct Prime Factors
def count_distinct_prime_factors(n):
    return len(set(prime_factors(n)))

# 12. Prime Power Check
def is_prime_power(n):
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime(p):
            k = 1
            while p**k <= n:
                if p**k == n:
                    return True
                k += 1
    return False
# Helper Prime Check
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

# 13. Mersenne Prime Check
def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    m = 2**p - 1
    return is_prime(m)

# 14. Twin Primes
def twin_primes(limit):
    twins = []
    for i in range(3, limit):
        if is_prime(i) and is_prime(i+2):
            twins.append((i, i+2))
    return twins

# 15. Number of Divisors
def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            count += 2 if i != n//i else 1
    return count

# 16. Aliquot Sum
def aliquot_sum(n):
    return sum(d for d in range(1, n) if n % d == 0)

# 17. Amicable Numbers
def are_amicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

# 18. Multiplicative Persistence
def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        prod = 1
        for d in str(n):
            prod *= int(d)
        n = prod
        steps += 1
    return steps

# 19. Highly Composite Number
def is_highly_composite(n):
    d_n = count_divisors(n)
    return all(count_divisors(i) < d_n for i in range(1, n))
# 20. Modular Exponentiation
def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

# 21. Modular Multiplicative Inverse
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

# 22. Chinese Remainder Theorem
def crt(remainders, moduli):
    M = math.prod(moduli)
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * mod_inverse(Mi, m)
    return x % M

# 23. Quadratic Residue Check
def is_quadratic_residue(a, p):
    return pow(a, (p-1)//2, p) == 1
# 24. Order Mod
def order_mod(a, n):
    for k in range(1, n):
        if pow(a, k, n) == 1:
            return k
    return None

# 25. Fibonacci Prime Check
def is_fibonacci_prime(n):
    return is_prime(n) and is_fibonacci(n)

def is_fibonacci(n):
    x1 = 5*n*n + 4
    x2 = 5*n*n - 4
    return int(math.sqrt(x1))*2 == x1 or int(math.sqrt(x2))*2 == x2

# 26. Lucas Sequence
def lucas_sequence(n):
    seq = [2, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# 27. Perfect Power Check
def is_perfect_power(n):
    for a in range(2, int(math.sqrt(n)) + 1):
        b = 2
        while a**b <= n:
            if a**b == n:
                return True
            b += 1
    return False

# 28. Collatz Length
def collatz_length(n):
    steps = 0
    while n != 1:
        n = n//2 if n % 2 == 0 else 3*n + 1
        steps += 1
    return steps

# 29. Polygonal Number
def polygonal_number(s, n):
    return ((s - 2)n(n - 1))//2 + n

# 30. Carmichael Number Check (Korselt's Criterion)
def is_carmichael(n):
    if n < 3 or is_prime(n):
        return False
    for a in range(2, n):
        if math.gcd(a, n) == 1 and pow(a, n-1, n) != 1:
            return False
    return True

# 31. Miller-Rabin Primality Test
def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    # write n-1 as d * 2^r
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

# 32. Pollard Rho Algorithm
def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x, y, c = 2, 2, 1
    f = lambda x: (x*x + c) % n
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
d = math.gcd(abs(x-y), n)
    return d if d != n else None

# 33. Zeta Function Approximation
def zeta_approx(s, terms):
    return sum(1 / (n**s) for n in range(1, terms+1))

# 34. Partition Function (Dynamic Programming)
def partition_function(n):
    p = [0] * (n+1)
    p[0] = 1
    for k in range(1, n+1):
        for i in range(k, n+1):
            p[i] += p[i-k]
    return p[n]
