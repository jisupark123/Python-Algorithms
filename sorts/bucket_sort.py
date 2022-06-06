"""
버킷 정렬

데이터가 균등 분포를 이룰 때 O(n)의 시간복잡도를 가지는 유용한 알고리즘이다.
하지만 O(n)뒤에 숨어있는 상수 인자가 매우 커서 실제로 구현해보면 균등 분포 데이터라도 퀵 정렬에 비해 더 느리다.

수행시간 - O(n) (하지만 실제로 구현해보면 퀵 정렬보다 느리다)
"""


def bucket_sort(lst: list) -> list:
    if len(lst) == 0:
        return []
    min_value, max_value = min(lst), max(lst)
    bucket_count = int(max_value - min_value) + 1
    buckets: list[list] = [[] for _ in range(bucket_count)]

    for i in lst:
        buckets[int(i - min_value)].append(i)

    return [v for bucket in buckets for v in sorted(bucket)]
