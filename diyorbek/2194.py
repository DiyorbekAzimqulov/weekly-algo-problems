from typing import List
"""
column is letter
row is integer

[column,row]
letters only from A-Z
integers only from 0-9
we need to get range from s[0] - s[3] -> it gives letters from and to
then we get the number range s[1] - s[4] it gives how many times 
we need to represent letters with corresponding numbers.


1. form list of letters
2. for each letter go through integer range
3. put string into result list
4. return result
"""

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        letters = [chr(letter) for letter in range(ord(s[0]), ord(s[3])+1)]
        nums = [num for num in range(int(s[1]), int(s[4]) + 1)]
        for letter in letters:
            for num in nums:
                element = letter + str(num)
                result.append(element)
        return result
