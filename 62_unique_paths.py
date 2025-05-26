class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
  
        memo={}
        def helper(r,c):
            if r==0 and c==0:
                return 1
            if r<0 or c<0:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)]=helper(r-1,c)+helper(r,c-1)
            return memo[(r,c)]
             
        return helper(m-1,n-1)