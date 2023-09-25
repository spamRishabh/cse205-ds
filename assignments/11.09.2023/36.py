class Solution(object):
    def isValidSudoku(self, board):

        def get_grid_index(row,col):
            return ((row // 3) * 3) + (col // 3)
        def number_is_valid(num):
            return 1 <= num <= 9

        row_data = {i: set() for i in range(9)}
        column_data = {i: set() for i in range(9)}
        grid_data = {i: set() for i in range(9)}
        
        for row_i, row in enumerate(board):
            for col_i, num in enumerate(row):
                if num != '.' and number_is_valid(int(num)):

                    grid_i = get_grid_index(row_i, col_i)

                    if num in column_data[col_i] or num in row_data[row_i] or num in grid_data[grid_i]: 
                        return False

                    column_data[col_i].add(num)
                    row_data[row_i].add(num)
                    grid_data[grid_i].add(num)

                    
        return True 