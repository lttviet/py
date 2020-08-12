from typing import List

def inverse_permutation(perm: List[int]) -> List[int]:
    for i in range(len(perm)):
        next = i

        temp_i = None
        temp = None

        while perm[next] >= 0:
            # after every pass, perm[next] is in right position
            temp = perm[next]

            try:               
                perm[next] = perm.index(next) - len(perm)                
            except ValueError:
                # not found, already modified
                perm[next] = temp_i - len(perm)
         
            temp_i = next
            next = temp

    return [p + len(perm) for p in perm]
        
if __name__ == '__main__':
    for perm in (
        [1,4,3,0,5,2], [0,1,2], 
        [1,3,5,0,2,4], [1,4,3,0,5,2]
    ):
        print(inverse_permutation(perm))