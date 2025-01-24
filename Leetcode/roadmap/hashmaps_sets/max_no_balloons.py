text = "loonbalxballpoon"
# text = "leetcode"


def maxNumberOfBalloons(text):
    balloon_dict = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
    dic = {}
    for t in text:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1

    max_balloons = float("inf")

    for char, count in balloon_dict.items():
        if char not in dic:
            return 0
        max_balloons = min(max_balloons, dic[char] // count)

    return max_balloons


sol = maxNumberOfBalloons(text)
print(sol)


# leetcode solution with 98% success rate
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # init HashMap (mp)
        text = text.lower()
        mp: dict = {}
        mp["b"] = 0
        mp["a"] = 0
        mp["l"] = 0
        mp["o"] = 0
        mp["n"] = 0

        # declare HashMap
        for txt in text:
            if txt in mp:
                mp[txt] += 1

        # return min -> bottleneck
        return min(mp["b"], mp["a"], mp["l"] // 2, mp["o"] // 2, mp["n"])
