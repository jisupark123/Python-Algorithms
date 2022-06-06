"""
계수 정렬

O(n)의 시간복잡도를 갖는 매우 효율적인 알고리즘
하지만 여러가지 제약을 갖는다. (배열의 인덱스를 이용해 데이터를 저장하기 때문)

* 데이터 값이 양수여야 한다. (코드를 간단히 조정해서 해결할 수 있다)
* 값의 범위가 너무 크지 않아야 한다. (임의의 원소 k의 크기가 O(n)을 초과하면 시간복잡도는 O(k)가 된다)

수행시간 
위의 조건을 만족할 경우 - O(n)
"""


def counting_sort(lst: list[int]) -> list[int]:
    if len(lst) == 0:
        return lst
    lst_max = max(lst)
    counting_lst = [0] * (lst_max + 1)
    for i in range(len(lst)):
        counting_lst[lst[i]] += 1
    for i in range(1, lst_max + 1):
        counting_lst[i] = counting_lst[i] + counting_lst[i - 1]

    res = [0] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        res[counting_lst[lst[i]] - 1] = lst[i]
        counting_lst[lst[i]] -= 1

    return res
