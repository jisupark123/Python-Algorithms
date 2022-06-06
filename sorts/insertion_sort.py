"""
삽입 정렬

수행시간 
최악의 경우 - O(n²)
평균 - O(n²)
최선의 경우(리스트가 이미(거의) 정렬된 상태로 입력되면) - O(n)

사전 작업으로 거의 정렬된 형태에 가깝게 만든 다음 삽입 정렬을 수행하면 굉장히 빠르다.
셸 정렬(shell_sort)이 삽입 정렬을 활용하는 대표적인 정렬 방법이다.
"""


def insertion_sort(lst) -> list:
    for i in range(1, len(lst)):
        temp_idx = i - 1
        insert_item = lst[i]
        # 이 지점에서 lst[0...i-1]은 이미 정렬된 상태다

        while temp_idx >= 0 and insert_item < lst[temp_idx]:
            lst[temp_idx + 1] = lst[temp_idx]
            temp_idx -= 1
        lst[temp_idx + 1] = insert_item

    return lst
