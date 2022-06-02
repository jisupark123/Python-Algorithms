def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp_idx = i - 1
        insert_item = lst[i]
        # 이 지점에서 lst[0...i-1]은 이미 정렬된 상태다

        while temp_idx >= 0 and insert_item < lst[temp_idx]:
            lst[temp_idx + 1] = lst[temp_idx]
            temp_idx -= 1
        lst[temp_idx + 1] = insert_item

    return lst


a = [200, 1, 4, 2, 3, 2, 1, 100, 8]
print(insertion_sort(a))
