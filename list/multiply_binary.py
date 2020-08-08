from typing import List

def multiply(n: List[int], m: List[int]) -> List[int]:
    res = [0] * (len(n) + len(m))

    sign = 1
    if n[0] * m[0] < 0:
        sign = -1

    n[0], m[0] = abs(n[0]), abs(m[0])

    for i in reversed(range(len(n))):
        for j in reversed(range(len(m))):
            res[i+j+1] += n[i] * m[j]
            res[i+j] += res[i+j+1] // 10
            res[i+j+1] %= 10

    res = res[next(
        (i for i, x in enumerate(res) if x != 0),
        len(res)
        ):] or [0]

    return [res[0] * sign] + res[1:]

if __name__ == '__main__':
    for num1, num2 in (
        ([-1,1], [1]), 
        ([1,2,3], [4,9])
    ):
        print(multiply(num1, num2))