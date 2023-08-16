
#

def bonAppetit(bill, k, b):
    # Write your code here
    total = 0
    for i in bill:
        total += i
    anna_bill = (total  - bill[k]) // 2
    # print(anna_bill)
    final_bill = b - anna_bill
    # print(final_bill)
    if final_bill ==  0:
        print('Bon Appetit')
    else:
        print(final_bill)   

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
