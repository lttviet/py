import math
from typing import List

def is_valid_sudoku(game: List[List[int]]) -> bool:
    def has_duplicates(block: List[int]) -> bool:
        block = list(filter(lambda x: x!= 0, block))
        return len(block) != len(set(block))
    
    n = len(game)
    # valid row
    for row in range(n):
        if has_duplicates(game[row]):
            return False

    # valid col
    for col in range(n):
        block = [game[row][col] for row in range(n)]
        if has_duplicates(block):
            return False

    # valid square
    size = int(math.sqrt(n))
    for i in range(size):
        for j in range(size):
            square = [
                game[row][col] 
                for row in range(size * i, size * (i+1))
                for col in range(size * j, size * (j+1))
            ]
            if has_duplicates(square):
                return False

    return True

if __name__ == '__main__':
    game1 = [[1,2,3,4], [1,0,0,0], [0,0,0,0], [0,0,0,0]]
    game2 = [[1,0,1,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    game3 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    game4 = [[1,2,3,4], [0,1,0,0], [0,0,0,0], [0,0,0,0]]

    print(is_valid_sudoku(game1))
    print(is_valid_sudoku(game2))
    print(is_valid_sudoku(game3))
    print(is_valid_sudoku(game4))
