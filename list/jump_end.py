from typing import List

def min_jump_end(lst: List[int]) -> bool:
    """Returns min num of jumps to reach end of list.
    """
    if len(lst) <= 1:
        return 0

    if lst[0] == 0:
        return -1

    max_reach, steps, jump = lst[0], lst[0], 1

    for i in range(1, len(lst)):
        if i == len(lst) - 1:
            return jump

        max_reach = max(max_reach, lst[i] + i)

        steps -= 1
        if steps == 0:
            jump += 1

            if i >= max_reach:
                return -1

            steps = max_reach - i

    return -1

if __name__ == '__main__':
    for lst in ([10,1,1,1], [3,3,1,0,2,0,1], [0,1], [1,1,1,1,1]):
        print(lst, min_jump_end(lst))