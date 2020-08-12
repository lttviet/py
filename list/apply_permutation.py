from typing import List

def apply(lst: List[str], perm: List[int]) -> List[int]:
    # https://stackoverflow.com/questions/16501424
    for i in range(len(perm)):
        next = i

        while perm[next] >= 0: # haven't swapped
            lst[i], lst[perm[next]] = lst[perm[next]], lst[i]
            temp = perm[next]

            # after every swap, lst[next] is in right position
            # negative to indicate done
            perm[next] -= len(perm) 
            next = temp

    perm = [p + len(perm) for p in perm]

    return lst
        
if __name__ == '__main__':
    for perm in ([0,1,2], [2,1,0], [0,2,1]):
        print(apply(['a', 'b', 'c'], perm))