from typing import List

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

        if s <= 1:
            carry = 0
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
    for num1, num2 in (
        ('1', '1'), ('0', '0'), ('111', '1111'), ('1111', '111')
    ):
        print(plus_binary(num1, num2))