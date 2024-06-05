# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         arr=[]

#         for i in s:
#             if
#                 if i not in arr:
#                     arr.append[i]
#                 else:
#                     arr=[]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
