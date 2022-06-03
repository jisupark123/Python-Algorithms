def counting_sort(lst: list) -> list:
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
