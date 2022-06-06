"""
버블 정렬

수행시간 - 모든 경우에 O(n²)
"""


def bubble_sort(lst):
    for i in range(len(lst), 0, -1):
        for j in range(i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
