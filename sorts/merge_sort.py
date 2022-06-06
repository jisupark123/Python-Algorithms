"""
병합 정렬

** 고급 정렬 알고리즘 **

최악의 경우에도 O(nlogn)의 성능을 보여주는 좋은 알고리즘이다.
알고리즘의 성능을 높이기 위해서 yield(제너레이터)를 사용했다.

수행시간 
모든 경우 - O(nlogn)
"""


def merge_sort(lst: list) -> list:

    # 정렬된 리스트 2개를 병합하는 함수
    def merge(left: list, right: list) -> list:
        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
