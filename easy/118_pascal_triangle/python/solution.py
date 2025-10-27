class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        triangle = [[1]]
        if numRows == 1:
            return triangle

        for row in range(1, numRows):
            row_list = []
            for i in range(0, row + 1):
                if i == 0 or i == row:
                    row_list.append(1)
                else:
                    row_list.append(triangle[row-1][i-1] + triangle[row-1][i])
            triangle.append(row_list)

        return triangle