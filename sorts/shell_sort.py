"""
셸 정렬

** 고급 정렬 알고리즘 **

삽입 정렬은 평균 O(n²)의 시간이 쇼요되지만 이미(거의) 정렬되어있으면 O(n)의 시간이 걸린다는 특징이 있다.
셸 정렬은 각 원소가 있어야 할 자리에서 멀리 떨어져 있을 가능성을 줄이는 작업을 하고(전처리) 마지막에 삽입 정렬로 끝난다.
간단한 전처리만 했을 뿐인데 삽입 정렬과 압도적인 성능 차이를 보여준다.

수행시간 
평균 - O(n^1.25)
"""


def shell_sort(lst: list) -> list:
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]  # 셸 정렬의 수행 시간은 gap 수열에 따라 편차가 있다
    for gap in gaps:
        for i in range(gap, len(lst)):
            insert_value = lst[i]
            j = i

            # while문의 순환 횟수가 전체 수행시간을 결정한다
            while j >= gap and lst[j - gap] > insert_value:
                lst[j] = lst[j - gap]
                j -= gap
            if j != i:
                lst[j] = insert_value

    return lst
