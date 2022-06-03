def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    pivot = lst.pop()
    greater: list[int] = []
    lesser: list[int] = []

    for element in lst:
        (greater if element > pivot else lesser).append(element)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)
