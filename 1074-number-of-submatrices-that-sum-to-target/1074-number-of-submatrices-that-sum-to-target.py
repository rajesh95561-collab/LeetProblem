class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0
        for i in range(rows):
            for j in range(1,cols):
                matrix[i][j] += matrix[i][j-1]

        for c1 in range(cols):
            for c2 in range(c1, cols):
                # Frequency map for 1D Subarray Sum Equals K pattern
                mapp = {0: 1}
                ps = 0
                
                # Iterate through all rows for current column span [c1, c2]
                for r in range(rows):
                    # Get 1D sum of row r between column c1 and c2
                    if c1 == 0:
                        row_sum = matrix[r][c2]
                    else:
                        row_sum = matrix[r][c2] - matrix[r][c1 - 1]
                    
                    ps += row_sum
                    need = ps - target
                    
                    if need in mapp:
                        count += mapp[need]
                        
                    mapp[ps] = mapp.get(ps, 0) + 1
                    
        return count