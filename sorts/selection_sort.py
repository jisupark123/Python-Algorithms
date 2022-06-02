def selection_Sort(lst: list):
    for last in range(len(lst) - 1, 0, -1):
        k = max_num(lst, last)  # lst[0...last] 중 가장 큰 수 lst[k] 찾기
        lst[k], lst[last] = lst[last], lst[k]

    return lst


# lst[0...last]에서 가장 큰 수의 인덱스를 리턴한다
def max_num(lst: list, last: int) -> int:
    largest = 0
    for i in range(last + 1):
        if lst[i] > lst[largest]:
            largest = i

    return largest
