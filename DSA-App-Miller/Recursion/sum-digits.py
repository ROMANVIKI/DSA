def sumDigits(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
print(sumDigits(472))



# q1 - 101 = 2**2 x 1 + 2 ** 1 x 0 + 2 ** 0 + 1 = 6
#
# q2 - 1111 = 2**3 x 1 + 2**2 x 1 + 2**1 x1 + 2**0x 1 = 14
#
# q3 - 10010 = 2**4 x1 + 2**3 x 0 = 2**2 x 0 + 2**1 x 1 + 2**0x 1 =18
#
# q4 - 6 = {
#     6/2 = 3 -remainder = 0 
#     3/2 = 1 -rem = 1
#     1/2 = 0 -rem = 1
# } = 011
#
# q5 - 9 = {
#     9/2 = 4 -rem = 1
#     4/2 = 2 -rem = 0
#     2/2 = 1 -rem = 0
#     1/2 = 0 -rem = 1
# } = 1001
#
# q6 - 20 = {
#     20/2 = 10 -rem = 0
#     10/2 = 5 -rem = 0
#     5/2 = 2 -rem = 1
#     1/2 = 0 -rem = 1
# } = 0011
#
# q7 - True
##
## q8 - False - because go go from right to left so the left first digit have have higher powever for example we 1001 the left first one woud have the value of 2**3
##
##
##
##Absolutely! Here's a fun and gradual **Binary Quiz** 🧠 with a mix of questions to test and reinforce your understanding. Let's go!
#
#---
#
### ✅ **PART 1: Binary to Decimal**
#
#Convert the following **binary numbers** to **decimal**.
#
#**Q1:** What is `101` in decimal?
#A. 4
#B. 5
#C. 6
#
#---
#
#**Q2:** What is `1111` in decimal?
#A. 14
#B. 15
#C. 16
#
#---
#
#**Q3:** What is `10010` in decimal?
#A. 18
#B. 20
#C. 22
#
#---
#
### ✅ **PART 2: Decimal to Binary**
#
#Convert the following **decimal numbers** to **binary**.
#
#**Q4:** What is `6` in binary?
#A. `101`
#B. `110`
#C. `111`
#
#---
#
#**Q5:** What is `9` in binary?
#A. `1001`
#B. `1010`
#C. `1100`
#
#---
#
#**Q6:** What is `20` in binary?
#A. `10100`
#B. `11010`
#C. `11100`
#
#---
#
### ✅ **PART 3: True or False**
#
#**Q7:** All binary numbers contain only digits 0 and 1.
#True or False?
#
#---
#
#**Q8:** In binary, the number rightmost is the most powerful digit.
#True or False?
#
#---
#
#Once you try answering, I’ll check them and explain everything in a friendly way! Ready when you are 😊

