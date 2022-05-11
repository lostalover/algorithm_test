class Solution:
    def countVowelStrings(self, n: int) -> int:
        aeiou = [1, 1, 1, 1, 1]
        
        for i in range(2, n+1):
            aeiou[0] = sum(aeiou[0:])
            aeiou[1] = sum(aeiou[1:])
            aeiou[2] = sum(aeiou[2:])
            aeiou[3] = sum(aeiou[3:])
            print(aeiou)

        return sum(aeiou)

Solution().countVowelStrings(3)
