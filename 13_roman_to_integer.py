"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
Given a roman number, convert it to an integer.
Ex: "MIX" -> 1009
"""

class Solution:
    def romanToInt(self, str):
        roman_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0
        prev = 0
        for char in str:
            cur = roman_to_value[char]
            result += cur
            if cur > prev:
                result -= 2 * prev
            prev = cur
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MIX"))