

def quick_sort(arr):
    if len(arr) < 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if  x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def birthdayCakeCandles(candles, candles_count):
    max_num = []
    sorted_list = quick_sort(candles)
    if sorted_list[candles_count - 1] == sorted_list[candles_count - 2] and sorted_list[candles_count - 3] == sorted_list[candles_count- 2]:
        print(3)
    elif sorted_list[candles_count - 1] == sorted_list[candles_count - 2]:
        print(2)
    elif sorted_list[candles_count - 1] > sorted_list[candles_count - 2]:
        print(1)
    else:
        print(0)


if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles, candles_count)
