# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if(sorted(s)==sorted(t)):
#             return True
#         else:
#             return False
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) !=len(t):
#             return False
        
#         countS ,countT ={},{}
         
#         for i in range(len(s)):
#             countS[s[i]]= 1+ countS.get(s[i],0)
#             countT[t[i]]= 1+ countT.get(t[i],0)

#         return countS==countT
class Solution:
    def isAnagram(self, s : str , t : str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap = defaultdict(int)
        for l in s:
            hashmap[l]+=1
        for l in t:
            if l not in hashmap:
                return False
            else:
                if hashmap[l]==0:
                    return False
                hashmap[l]-=1
        return True    

