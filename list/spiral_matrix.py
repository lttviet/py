import math
from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    MOVES = ((0,1), (1,0), (0,-1), (-1,0))
    row = col = direction = 0
    spiral = []

    for _ in range(len(matrix) ** 2):
        spiral.append(matrix[row][col])
        matrix[row][col] = None
        next_row, next_col = row + MOVES[direction][0], col + MOVES[direction][1]        
        
        if (
                next_row not in range(len(matrix)) or 
                next_col not in range(len(matrix)) or 
                not matrix[next_row][next_col]
        ):
            direction = (direction + 1) % len(MOVES)
            next_row, next_col = row + MOVES[direction][0], col + MOVES[direction][1]

        row, col = next_row, next_col
    return spiral

def spiral_to_matrix(d: int) -> List[List[int]]:
    """Return a matrix dxd which has spiral order (1,2,...d**2).
    """
    MOVES = ((0,1), (1,0), (0,-1), (-1,0))
    row = col = direction = 0
    matrix = [[0 for _ in range(d)] for _ in range(d)]

    for num in range(1, d**2 + 1):
        matrix[row][col] = num
        next_row, next_col = row + MOVES[direction][0], col + MOVES[direction][1]

        if (
                next_row not in range(d) or
                next_col not in range(d) or
                matrix[next_row][next_col] != 0
        ):
            direction = (direction + 1) % len(MOVES)
            next_row, next_col = row + MOVES[direction][0], col + MOVES[direction][1]

        row, col = next_row, next_col

    return matrix

def spiral_array_to_matrix(spiral: List[int]) -> List[List[int]]:
    MOVES = ((0,1), (1,0), (0,-1), (-1,0))
    row = col = direction = 0

    d = int(math.sqrt(len(spiral)))
    matrix = [[None for _ in range(d)] for _ in range(d)]

    for _, val in enumerate(spiral):
        matrix[row][col] = val
        next_row, next_col = row + MOVES[direction][0], col + MOVES[direction][1]


        if (
            next_row not in range(d) or
            next_col not in range(d) or
            matrix[next_row][next_col] != None
        ):
            direction = (direction + 1) % len(MOVES)
            next_row, next_col = row + MOVES[direction][0], col + MOVES[direction][1]  

        row, col = next_row, next_col

    return matrix


if __name__ == '__main__':
    matrices = (
        [[1,2], [3,4]], 
        [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]],
        [[1,2,3], [4,5,6], [7,8,9]]
    )

    print('### Spiral matrix')
    for m in matrices:
        print(spiral_matrix(m))

    print('### Spiral to matrix')
    print(spiral_to_matrix(3))

    print('### Spiral array to matrix')
    spirals = (
        [1,2,3,6,9,8,7,4,5],
        [1,2,3,4,5,6,7,8,9]
    )
    for s in spirals:        
        print(spiral_array_to_matrix(s))