class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row=len(matrix)
        column=len(matrix[0])
        top=0
        bottom=row-1
        left=0
        right=column-1
        ans=[]
        
        while (top<=bottom and left<=right):
                i=left
                while i<=right:
                        ans.append(matrix[top][i])
                        i+=1
                top+=1
                i=top
                while (i<=bottom):
                        ans.append(matrix[i][right])
                        i+=1
                right-=1
                if top<=bottom:
                        i=right
                        while i>=left:
                                ans.append(matrix[bottom][i])
                                i-=1
                        bottom-=1
                if left<=right:
                        i=bottom
                        while i>=top:
                                ans.append(matrix[i][left])
                                i-=1
                        left+=1
        return ans

                
                        
        