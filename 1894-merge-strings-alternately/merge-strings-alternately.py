# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         n=len(word1)
#         m=len(word2)
#         l1,r1=0,n-1
#         l2,r2=0,m-1
#         merged=""
#         for i in range(m+n-1):
#             if l1<=l2 and l1<=r1:
#                 "".join([merged,word1[l1]])
#                 l1+=1
#             else:
#                 "".join([merged,word2[l2]])
#                 l2+=1
#         return merged
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        merged = []
        i = 0
        j = 0

        # Alternately merge characters from both strings
        while i < n or j < m:
            if i < n:
                merged.append(word1[i])
                i += 1
            if j < m:
                merged.append(word2[j])
                j += 1
        
        # Join the list into a single string and return it
        return ''.join(merged)
