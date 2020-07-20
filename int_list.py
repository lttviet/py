from typing import List


def plus_one(lst: List[int]) -> List:
    """Take a list of integers, which represents a decimal number N.
    Returns the list that represents N+1
    """
    lst[-1] += 1
    
    for i in reversed(range(1, len(lst))):
        if lst[i] != 10:
            break
        lst[i] = 0
        lst[i-1] += 1

    if lst[0] == 10:
        lst[0] = 0
        lst.insert(0, 1)

    return lst

def plus_binary(num1: str, num2: str) -> str:
    """Add 2 binary numbers in the form of string
    """
    if len(num1) < len(num2):
        num1 = '0' * (len(num2) - len(num1)) + num1
    else:
        num2 = '0' * (len(num1) - len(num2)) + num2

    result = ''
    carry = 0
    for i in reversed(range(len(num1))):
        s = int(num1[i]) + int(num2[i]) + carry
        carry -= 1

        if s <= 1:
            result = str(s) + result
        elif s == 2:
            carry = 1
            result = '0' + result
        else:
            carry = 1
            result = '1' + result

    if carry == 1:
        result = '1' + result

    return result
         

if __name__ == '__main__':
    for lst in ([1,2,3], [0], [9], [9,9], [1,0,0]):
        print(plus_one(lst))

    for num1, num2 in (
        ('1', '1'), ('0', '0'), ('111', '1111'), ('1111', '111')
    ):
        print(plus_binary(num1, num2))