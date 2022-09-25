def reverse(arr):
        i=0
        j=len(arr)-1
        while i<=j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        return arr
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        
        for i in range (n):
                for j in range (i):
                        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
                reverse(i)
        return matrix
                
        