"""
선택 정렬

수행시간 - 모든 경우에 O(n²)
"""


def selection_sort(lst: list) -> list:

    # lst[0...last]에서 가장 큰 수의 인덱스를 리턴한다
    def max_num(lst: list, last: int) -> int:
        largest = 0
        for i in range(last + 1):
            if lst[i] > lst[largest]:
                largest = i
        return largest

    for last in range(len(lst) - 1, 0, -1):
        k = max_num(lst, last)  # lst[0...last] 중 가장 큰 수 lst[k] 찾기
        lst[k], lst[last] = lst[last], lst[k]

    return lst
