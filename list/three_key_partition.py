from typing import List

def three_key_partition(lst: List[int]) -> List[int]:
    """Every element in lst belong to 1 of 3 keys (RED, GREEN, BLUE).
    Reorder the list so element of the same key are together.
    Order of sub array doesn't matter.
    """
    # lst[:red] red
    # lst[red:green] green
    # lst[green:blue] unclassified
    # lst[blue:] blue
    red, green, blue = 0, 0, len(lst)

    R, G, B = range(3)

    while green < blue:
        if lst[green] == R:
            lst[red], lst[green] = lst[green], lst[red]
            red += 1
            green += 1
        elif lst[green] == G:
            green += 1
        else:
            blue -= 1
            lst[green], lst[blue] = lst[blue], lst[green]

    return lst

if __name__ == '__main__':
    RED, GREEN, BLUE = range(3)
    lists = ([RED, GREEN, RED, BLUE, BLUE, RED], [RED, BLUE, RED])
    for lst in lists:
        print(three_key_partition(lst))