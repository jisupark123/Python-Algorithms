"""
힙 정렬

** 고급 정렬 알고리즘 **

최악의 경우에도 O(nlogn)의 성능을 보여주는 좋은 알고리즘이다.
힙 자료구조를 사용해서 정렬한다.

수행시간 
모든 경우 - O(nlogn)
"""


def heap_sort(lst: list) -> list:
    def build_heap():
        for i in range((len(lst) - 2) // 2, -1, -1):
            percolate_down(i, len(lst) - 1)

    def percolate_down(k: int, end: int):
        child = 2 * k + 1  # 왼자식
        right = 2 * k + 2  # 오른자식
        if child <= end:
            if right <= end and lst[child] < lst[right]:
                child = right

            if lst[k] < lst[child]:
                lst[k], lst[child] = lst[child], lst[k]
                percolate_down(child, end)

    build_heap()
    for last in range(len(lst) - 1, 0, -1):
        lst[last], lst[0] = lst[0], lst[last]
        percolate_down(0, last - 1)

    return lst
