"""
to find the maximum distance we need to calculate 
starting position with end position and if colors are same then decrease distance

two pointer technique
1 pointer is starting from the beginning
2 pointer is starting from the end
we need to have threshold value for comparison

[1,8,3,8,3]
 ^       ^
we start from the first element
second pointer starts from the last element
here we need to define what can be the maximum distance
it is length of the list - position of first pointer
if colors are different and length is threshold length then we do not need to 
look at other comparisons


iterate over an entire list
for each number it is marked as start pointer
and last element is last pointer
we also here define threshold max distance it is abs(last-start)
if colors are different and it is equal to threshold then return. 
otherwise keep track of max distance and return in the end.
"""
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i = 0
        result = -1
        while i < len(colors):
            j = len(colors) - 1
            while j > i:
                if colors[i] != colors[j]:
                    result = max(result, abs(i-j))
                    break
                else:
                    j -= 1
            i += 1
        return result
        
