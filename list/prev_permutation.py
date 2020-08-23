from typing import List

# if I have a sub list of ascending order, it's the smallest value
# find inversion point just before the sub list
# swap the biggest val in sub list that < inversion
# reverse the sub list to make it biggest

def prev_permutation(perm: List[int]) -> List[int]:
    # find inversion point perm[i] > perm[i+1]
    i = len(perm) - 2
    while (i >= 0 and perm[i] <= perm[i+1]):
        i -= 1

    if i == -1:
        return []

    # swap perm[i] with biggest val after perm[i]
    # that < perm[i]
    for j in reversed(range(len(perm))):
        if perm[j] < perm[i]:
            perm[j], perm[i] = perm[i], perm[j]
            break

    perm[i+1:] = reversed(perm[i+1:])
    return perm
        
if __name__ == '__main__':
    for perm in ([0,1,2], [2,1,0], [0,2,1]):
        print(prev_permutation(perm))