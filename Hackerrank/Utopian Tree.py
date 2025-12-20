def utopianTree(n):
    height = 1
    for cycle in range(n):
        if cycle % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

        
    


if __name__ == '__main__':
   

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(result)














