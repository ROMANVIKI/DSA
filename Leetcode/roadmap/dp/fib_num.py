class Solution:

    def fib(self, n):
        if n <= 1:
            return n
        a, b = (
            0,
            1,
        )  # so wer're not going to calculate the 0 and 1 since we know they return the same value as they hold
        # so we started off with the values
        for _ in range(
            2, n + 1
        ):  # so we start from 2 since we have prev two values as a, b
            a, b = (
                b,
                a + b,
            )  # as we started the loop find the fib(2) which is 0 + 1 so we change the a value to b and b value to a + b
        return b  # finally we return b as it holds the fib value


sol = Solution()
print(sol.fib(n=19))
