def bubble_Sort(lst):
    for i in range(len(lst), 0, -1):
        for j in range(i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
