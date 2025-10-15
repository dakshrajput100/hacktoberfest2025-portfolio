class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = sorted(strs)
        a = strr[0]
        b = strr[-1]
        c = ""
        for i in range(len(a)):
             
            if a[i] != b[i]:
                return(c)
            else:    
                c = c + a[i]
               
        return(c)       
