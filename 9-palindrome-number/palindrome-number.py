class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        # Convert the number to a string
        y = str(x)
        
        # Compare the string to its reverse
        return y == y[::-1]
