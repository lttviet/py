from typing import List

def find_primes(n: int) -> List[int]:
    """Find all prime nums up to n
    """
    primes = []

    if n < 2:
        return primes

    is_prime = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            # multiple of prime are not prime
            # start from i^2 instead of i*2 to ignore even nums
            for j in range(i**2, n + 1, i):
                is_prime[j] = False

    return primes


if __name__ == '__main__':
    for i in (10,1,2,3,4,24):
        print(i, find_primes(i))