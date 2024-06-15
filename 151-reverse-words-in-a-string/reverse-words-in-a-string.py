# class Solution:
#     def reverseWords(self, s: str) -> str:
#         slist=s.split(" ")
#         n=len(slist)
#         l=0
#         r=n-1
#         while l<r:
#             slist[l],slist[r]=slist[r],slist[l]
#             l+=1
#             r-=1
#         s=" ".join(slist)
#         return s
class Solution:
    def reverseWords(self, s: str) -> str:
        """
            Input: s: str
            Return: str
        """
        return " ".join(map(str, s.split()[::-1]))