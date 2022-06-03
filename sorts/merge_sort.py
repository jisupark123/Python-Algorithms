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


a = [3, 1, 10, 5, 2]

print(merge_sort(a))
