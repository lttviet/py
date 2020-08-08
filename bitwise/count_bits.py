def count_bits(x: int) -> int:
    """Returns the number of bits that are 1.
    """
    num_bit: int = 0
    while x:
        # if odd, right most bit is 1
        num_bit += x & 1
        # shift to the right 1 bit
        x >>= 1

    return num_bit

if __name__ == '__main__':
    for i in (1, 2, 11):
        print(i, count_bits(i))