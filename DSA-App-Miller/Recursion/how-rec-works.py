def recursion_func(n):
    if n < 1:
        print('n is less than 1')
    else:
        recursion_func(n-1)
        print(n)

print(recursion_func(4))

# Recustion uses stack memory - LIFO Principle
#
# so first recursion_func(4) --- stored in the stack memory
# then recursion_func(3) and so on 
# after the storing the functions in stack memory
# it get executed according to the LIFO Principle (Last In First Out)
# so first recursion_func(0) gets executed - recursion_func(4)
#
# output : 
# n is less than 1
# 1
# 2
# 3
# 4
# None
