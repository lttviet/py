from typing import List

def four_key_partition(lst: List[int]) -> List[int]:
    """Every element in lst belong to 1 of 3 keys (RED, GREEN, BLUE).
    Reorder the list so element of the same key are together.
    Order of sub array doesn't matter.
    """
    # lst[:red] red
    # lst[red:green] green
    # lst[green:blue] blue
    # lst[blue:yellow] unclassified
    # lst[yellow:] yellow
    red, green, blue, yellow = 0, 0, 0, len(lst)

    R, G, B, Y = range(4)

    while blue < yellow:
        if lst[blue] == R:
            lst[red], lst[blue] = lst[blue], lst[red]
            red += 1
            green += 1
            blue += 1
        elif lst[blue] == G:
            lst[green], lst[blue] = lst[blue], lst[green]
            green += 1
            blue += 1
        elif lst[blue] == B:
            blue += 1
        else:x
            yellow -= 1
            lst[blue], lst[yellow] = lst[yellow], lst[blue]

    return lst

if __name__ == '__main__':
    RED, GREEN, BLUE, YELLOW = range(4)
    lists = (
        [RED, YELLOW, GREEN, RED, YELLOW, YELLOW, BLUE, BLUE, RED], 
        [RED]
    )
    for lst in lists:
        print(four_key_partition(lst))