class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        return self.generate(rowIndex + 1)[rowIndex]
        
    def generate(self, rowIndex):
        triangle = [[1]]
        if rowIndex == 1:
            return triangle

        for row in range(1, rowIndex):
            row_list = []
            for i in range(0, row + 1):
                if i == 0 or i == row:
                    row_list.append(1)
                else:
                    row_list.append(triangle[row-1][i-1] + triangle[row-1][i])
            triangle.append(row_list)

        return triangle
