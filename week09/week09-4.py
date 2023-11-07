class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        a = arr
        N = len(a)
        for i in range(N-1):
            d = a[1] - a[0]
            if a[i+1] - a[i] != d
                return False
                
        return True       