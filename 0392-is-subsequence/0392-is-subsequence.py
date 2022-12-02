# def helper(t):
        
#         if len(t)==0:
#                 output=[]
#                 output.append('')
#                 return output 
        
#         new_output=[]
        
#         small_output=helper(t[1:])
        
#         for sub in small_output:
#                 new_output.append(sub)
                
#         for i in small_output:
#                 new_output.append(t[0]+i)
                
#         return new_output 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        m,n=len(s),len(t)
        c=a=0
        for i in range(m):
            for j in range(a,n):
                if s[i]==t[j]:
                    a=j+1
                    c+=1
                    break
        if c==m:
            return True
        return False
        
#         ans=helper(t)
        
#         if s in ans:
#                 return True 
#         return False 