def elimination(arr):
    compare_list = []
    for num in arr:
        if num in compare_list:
            return num
        compare_list.append(num)
    return
