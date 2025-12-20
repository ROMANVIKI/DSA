def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc == wc or (z > bc and z > wc) :
        return b*bc + w*wc
    elif bc <= wc and (bc + z) <= wc:
        
        return b*bc + w*(bc+z)
    elif bc > wc and (wc + z) <= bc:
        return b*(wc + z) + w*wc  
    elif bc < wc and (wc + z) > bc:
        return b*bc + w*wc
    elif bc > wc and (bc + z) > wc:
        return b*bc + w*wc
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(result)
