from typing import List

def even_odd(lst: List[int]) -> List[int]:
    """Reorder list to have even numbers appear first.
    """
    even, odd = 0, len(lst) - 1
    while even < odd:
        if lst[even] % 2 == 0:
            even += 1
        else:
            lst[even], lst[odd] = lst[odd], lst[even]
            odd -= 1

def even_odd_python(lst: List[int]) -> List[int]:
    lst.sort(key=lambda x: x%2)

def dutch_flag_partition(lst, index):
    """Reorder to less than lst[index], equal to lst[index] and higher than lst[index]
    """
    pivot = lst[index]
    # lst[:smaller] smaller than
    # lst[smaller:equal] equal to
    # lst[equal:higher] unclassified
    # lst[higher:] higher than
    smaller, equal, higher = 0, 0, len(lst)

    while equal < higher: # loop as long as there're unclassified
        # lst[equal] unclassified variable
        if lst[equal] < pivot:
            lst[equal], lst[smaller] = lst[smaller], lst[equal]
            smaller += 1
            equal += 1
        elif lst[equal] == pivot:
            equal += 1
        else:
            higher -= 1
            lst[equal], lst[higher] = lst[higher], lst[equal]

def three_key_partition(lst: List[int]):
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

def four_key_partition(lst: List[int]):
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


def reorder_false_true(lst: List[bool]):
    """Reorder a list of booleans to have false first.
    """
    # lst[:f] false
    # lst[f:t] unclassified
    # lst[t:] true
    f, t = 0, len(lst)
    while f < t:
        if not lst[f]:
            f += 1
        else:
            t -= 1
            lst[f], lst[t] = lst[t], lst[f]

def reorder_false_true_relative_order_true(lst: List[bool]) -> None:
    """ Reorder array to have false first then true.
    Keep the relative order of true.
    """
    # https://stackoverflow.com/questions/29723998
    # idea is to avoid swapping 2 true elements
    # loop from the end to beginning
    # lst[t:] true
    t = len(lst)
    for i in range(len(lst)-1, -1, -1):
        if lst[i]:
            t -= 1
            lst[i], lst[t] = lst[t], lst[i]

if __name__ == '__main__':
    lists = ([1,2,3], [], [2], [3,3], [4,4], [1,2,3,4,5,6,7,8,9])
    for lst in lists:
        even_odd_python(lst)
        print(lst)

    RED, GREEN, BLUE = range(3)
    lists = ([RED, GREEN, RED, BLUE, BLUE, RED], [RED, BLUE, RED])
    for lst in lists:
        three_key_partition(lst)
        print(lst)