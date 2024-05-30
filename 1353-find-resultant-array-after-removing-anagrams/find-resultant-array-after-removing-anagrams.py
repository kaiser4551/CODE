# class Solution:
#     def isAnagram(self, s : str , t : str) -> bool:
#         if len(s)!=len(t):
#             return False
#         hashmap = defaultdict(int)
#         for l in s:
#             hashmap[l]+=1
#         for l in t:
#             if l not in hashmap:
#                 return False
#             else:
#                 if hashmap[l]==0:
#                     return False
#                 hashmap[l]-=1
#         return True 
#     def removeAnagrams(self, words: List[str]) -> List[str]:
#         l=[]
#         solution=Solution()
#         for i in range(1,len(words)):
#             if solution.isAnagram(words[i],words[i-1]) is True or (words[i] not in l and words[i-1] not in l) :
#                 l.append(words[i-1])
#         return l
class Solution:
    def anagrams(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)
    
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for i in range(1, len(words)):
            if not self.anagrams(words[i], words[i-1]):
                res.append(words[i])
        return res