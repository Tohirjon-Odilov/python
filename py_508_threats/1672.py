# 1672. Richest Customer Wealth
if 0:
    class Solution:
        def maximumWealth(self, accounts: list[list[int]]) -> int:
            return max(list(map(sum, accounts)))
        
    print(Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

# 566. Reshape the Matrix
if 1:
    # Time Complexity : O(r*c)
    # Space Complexity : O(r*c)
    class Solution(object):
        def matrixReshape(self, mat, r, c):
            # Base case...
            if not mat: return mat
            # If transformation doesn't occur, return mat...
            if len(mat) * len(mat[0]) != r * c:
                print(len(mat)*len(mat[0]), r*c)
                return mat
            # Otherwise create a output matrix and fill the cells...
            output = [[0 for i in range(c)] for i in range(r)]
            idx = 0
            # Traverse the matrix through the loop... 
            while idx < r * c:
                # idx % c will give us the current column number...
                # idx / c will give us how many rows we have completely filled...
                output[idx // c][ idx % c] =  mat[idx // len(mat[0])][idx % len(mat[0])]
                idx += 1
            return output       # Return the output matrix...
        
    
    print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
    print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))