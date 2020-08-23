from typing import List

# if I have a sub list of descending order, it's the biggest val
# find the inversion point just before this sub list
# swap it with smallest val in sub list that > inversion
# reverse sub list to make it the smallest number

def next_permutation(perm: List[int]) -> List[int]:
    # find inversion point perm[i] < perm[i+1]
    i = len(perm) - 2
    while (i >= 0 and perm[i] >= perm[i + 1]):
        i -= 1

    if i == -1:
        return []

    # swap smallest element after inversion point with perm[i]
    # that > perm[i]
    for j in reversed(range(i + 1, len(perm))):
        if perm[j] > perm[i]:
            perm[i], perm[j] = perm[j], perm[i]
            break

    # reverse after perm[i]
    perm[i+1:] = reversed(perm[i+1:])

    return perm
        
if __name__ == '__main__':
    for perm in ([0,1,2], [2,1,0], [0,2,1]):
        print(next_permutation(perm))