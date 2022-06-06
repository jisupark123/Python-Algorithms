"""
기수 정렬

데이터의 각 자릿수를 낮은 자리수에서부터 가장 큰 자리수까지 올라가면서 정렬을 수행한다.
원소들이 모두 상수 k개 이하의 자릿수를 가진 자연수와 같은 특수한 경우에 사용할 수 있는 방법이며 O(n)의 시간이 소요된다.


수행시간 
RADIX가 상수일 때 - O(n)
"""


def radix_sort(lst: list[int]) -> list[int]:
    if len(lst) == 0:
        return lst
    RADIX = 10  # (RADIX가 상수가 아니라면 기수 정렬은 매력이 없다)
    placement = 1
    max_digit = max(lst)
    while placement <= max_digit:
        # declare and initialize empty buckets
        buckets: list[list] = [list() for _ in range(RADIX)]
        # split lst between the buckets
        for i in lst:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        # put each buckets' contents into lst
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                lst[a] = i
                a += 1
        # move to next
        placement *= RADIX
    return lst
