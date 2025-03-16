def lonelyinteger(a):
    # Write your code here
    uniq_dic = {}
    for num in a:
        if num in uniq_dic:
            uniq_dic[num] += 1
        else:
            uniq_dic[num] = 1
    for j in uniq_dic:
        if uniq_dic[j] == 1:
            return j


sol = lonelyinteger(a=[1, 2, 3, 4, 3, 2, 1])
print(sol)
