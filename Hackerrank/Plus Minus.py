def plusMinus(arr):
    positive_digit = 0
    negative_digit = 0
    neutral_digit = 0
    for digit in arr:
        if digit > 0:
            positive_digit += 1
        elif digit < 0:
            negative_digit += 1
        else:
            neutral_digit += 1
    ratio_positive_digit = positive_digit / len(arr)
    ratio_negative_digit = negative_digit / len(arr)
    ratio_neutral_digit = neutral_digit / len(arr)

    print("{:.6f}".format(ratio_positive_digit))
    print("{:.6f}".format(ratio_negative_digit))
    print("{:.6f}".format(ratio_neutral_digit))

plusMinus(arr)


