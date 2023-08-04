def birthdayCakeCandles(candles):
    # Initialize a variable to store the maximum height
    max_height = candles[0]

    # Iterate through the list of candles to find the maximum height
    for height in candles:
        if height > max_height:
            max_height = height

    # Count how many candles have the maximum height
    count_tallest = 0
    for height in candles:
        if height == max_height:
            count_tallest += 1

    return count_tallest

if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
