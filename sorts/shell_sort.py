def shell_sort(lst: list) -> list:
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(lst)):
            insert_value = lst[i]
            j = i
            while j >= gap and lst[j - gap] > insert_value:
                lst[j] = lst[j - gap]
                j -= gap
            if j != i:
                lst[j] = insert_value

    return lst


print(shell_sort([100, 5, 2, 6, 29, 35, 14, 60, 1, 5]))
