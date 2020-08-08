def parity(x: int) -> int:
    """Returns 1 if number of 1s is odd, 0 otherwise.
    """
    res = 0
    while x:
        # exclusive or
        # if y = 0, returns x. Else returns complement of x
        res ^= x & 1
        x >>= 1

    return res

if __name__ == '__main__':
    for i in (1, 2, 11):
        print(i, parity(i))