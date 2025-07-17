def find_max(list_a):
    if len(list_a) == 1:
        return 1 
    max_num = find_max[1:] 
    if list_a[0] > max_num:
        return list_a[0]

