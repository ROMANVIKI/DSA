import sys

input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        result = []
        max_beauty = 0

        # Keep only a sliding window of recent elements
        window = []

        for i in range(n):
            current_max = max_beauty

            # Check current element against elements in window
            for prev_val in window:
                f_val = (a[i] % prev_val) + (prev_val % a[i])
                current_max = max(current_max, f_val)

            # Add current element to window
            window.append(a[i])

            # Keep window size manageable - only keep last K elements
            # This is the key optimization
            K = min(320, i + 1)  # Adjust K based on constraints
            if len(window) > K:
                window.pop(0)

            max_beauty = current_max
            result.append(max_beauty)

        print(" ".join(map(str, result)))


solve()
