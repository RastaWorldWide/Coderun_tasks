class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        result = 0
        s += " "
        for index, i in enumerate(s):
            if s[index + 1] == " ":
                result += roman_to_int[i]
                return result

            if roman_to_int[s[index]] >= roman_to_int[s[index + 1]]:
                result += roman_to_int[i]
            else:
                result -= roman_to_int[i]


sol = Solution()

user = input()

print(sol.romanToInt(user))