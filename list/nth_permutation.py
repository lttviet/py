from typing import List

# https://medium.com/@aiswaryamathur/find-the-n-th-permutation-of-an-ordered-string-using-factorial-number-system-9c81e34ab0c8
# I still don't really understand the algorithm

def to_factorial(num: int) -> List[int]:
    """Returns the factorial form of a number.
    """
    fact = []

    for i in range(1, num):
        if num <= 0:
            break

        fact.insert(0, num % i)
        num = num // i

    return fact

def get_permutation(identity: List, n: int) -> List[int]:
    """Gets nth permutation starting from identity permutation.
    """
    fact = to_factorial(n)
    perm = []

    for i in fact:
        perm.append(identity[i])
        identity.pop(i)

    return perm
        
if __name__ == '__main__':    
    print(get_permutation(['a', 'b', 'c', 'd'], 14))
    print(get_permutation([0,1,2,3,4,5,6,7,8,9], 3628799))