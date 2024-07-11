# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         tsum=0
#         for i in range(len(s)-1):
#             if s[i]=="M":
#                 tsum+=1000
#             elif s[i]=="D":
#                 tsum+=500
#             elif s[i]=="C":
#                 if s[i+1]=="M" or s[i+1]=="D":
#                     tsum-=100
#                 else:
#                     tsum+=100
#             elif s[i]=="L":
#                 tsum+=50
#             elif s[i]=="X":
#                 if s[i+1]=="C" or s[i+1]=="L":
#                     tsum-=10
#                 else:
#                     tsum+=10
#             elif s[i]=="V":
#                 tsum+=5
#             elif s[i]=="I":
#                 if s[i+1]=="X" or s[i+1]=="V":
#                     tsum-=1
#                 else:
#                     tsum+=1
#         return tsum
class Solution:
    def romanToInt(self, s: str) -> int:
        total_sum = 0
        n = len(s)
        
        for i in range(n - 1):
            if s[i] == 'M':
                total_sum += 1000
            elif s[i] == 'D':
                total_sum += 500
            elif s[i] == 'C':
                if s[i + 1] == 'M' or s[i + 1] == 'D':
                    total_sum -= 100
                else:
                    total_sum += 100
            elif s[i] == 'L':
                total_sum += 50
            elif s[i] == 'X':
                if s[i + 1] == 'C' or s[i + 1] == 'L':
                    total_sum -= 10
                else:
                    total_sum += 10
            elif s[i] == 'V':
                total_sum += 5
            elif s[i] == 'I':
                if s[i + 1] == 'X' or s[i + 1] == 'V':
                    total_sum -= 1
                else:
                    total_sum += 1
        
        # Add the value of the last character
        if s[-1] == 'M':
            total_sum += 1000
        elif s[-1] == 'D':
            total_sum += 500
        elif s[-1] == 'C':
            total_sum += 100
        elif s[-1] == 'L':
            total_sum += 50
        elif s[-1] == 'X':
            total_sum += 10
        elif s[-1] == 'V':
            total_sum += 5
        elif s[-1] == 'I':
            total_sum += 1
        
        return total_sum
