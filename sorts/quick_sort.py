"""
퀵 정렬

** 고급 정렬 알고리즘 **
최악의 경우에 O(n²)의 시간이 쇼요되지만 평균 성능은 매우 빨라 실무에서 많이 사용된다.

최악의 경우
* 입력이 (거의)정렬되어 있을 때 (역순으로 정렬되어있을 때도 마찬가지다) -> 기준 원소를 잡을 때 맨 앞이나 맨 뒤의 원소를 잡지 말고 임의의 한 원소를 고르면 해결된다.
* 동일한 원소가 많이 존재하는 경우 -> (동일한 원소를 만나면 양쪽에 골고루 나누어주도록 변경해서 해결할 수 있다)

수행시간 
최악의 경우 - O(n²)
평균 - O(nlogn)
"""


def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst
    pivot = lst.pop()
    greater: list[int] = []
    lesser: list[int] = []

    for element in lst:
        (greater if element > pivot else lesser).append(element)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)
