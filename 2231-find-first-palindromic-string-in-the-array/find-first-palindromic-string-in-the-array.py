# class Solution:
    
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()

#         left, right = 0, len(s)-1
#         while left < right:
#             if not s[left].isalnum():
#                 left += 1            
#             elif not s[right].isalnum():
#                 right -= 1            
#             else:
#                 if s[left] != s[right]:
#                     return False
#                 else:
#                     left += 1
#                     right -= 1
#         return True 

#     def firstPalindrome(self, words: List[str]) -> str:
#         for i in range(len(words)):
#             if self.isPalindrome(words[i]) is True:
#                 return words[i]
#         return ""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i[::-1] == i:
                return i
        return ""   