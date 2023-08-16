
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    no_oranges = 0
    no_apples = 0
    apple_list = []
    orange_list = []

    for apple in apples:
        apple_list.append(a+apple)
    

    for orange in oranges:
        orange_list.append(b+orange)
    # print(apple_list)
    # print(orange_list)
    for i in apple_list:
        if i >= s and i <= t:
            no_apples += 1
    
    for j in orange_list:
        if j >= s and j <= t:
            no_oranges += 1
    
    # total_list[0] = no_apples
    # total_list.append(no_oranges)
    # for ans in total_list:
        
    #     n = ''
    #     return ans
    print(no_apples)
    print(no_oranges)
         
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
