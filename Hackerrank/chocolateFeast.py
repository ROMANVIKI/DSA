def chocolateFeast(n, c, m):
    chocolate_count = n // c
    wrappers = chocolate_count

    while wrappers >= m:
        free = wrappers // m
        chocolate_count += free
        wrappers = wrappers % m + free

    return chocolate_count


if __name__ == "__main__":
    test_cases = int(input().strip())
    for _ in range(test_cases):
        n, c, m = map(int, input().strip().split())
        print(chocolateFeast(n, c, m))
