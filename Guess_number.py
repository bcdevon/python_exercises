class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while high >= low:
            middle = (high + low)//2
            if guess(middle) == -1:
                high = middle - 1
            elif guess(middle) == 1:
                low = middle + 1
            elif guess(middle) == 0:
                return middle