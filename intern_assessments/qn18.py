def mergeTwoList(list1, list2):

    merged_list = []
    for x in list1:
        merged_list.append(x)

    for y in list2:
        merged_list.append(y)
    return sorted(merged_list)


sol = mergeTwoList(list1=[1, 3, 5, 7], list2=[2, 4, 6, 8])
print(sol)
