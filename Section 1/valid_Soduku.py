"""
    Exam Link: https://www.interviewbit.com/problems/valid-sudoku/

    Question:

    Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

    The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.

    image of Sudoku is in folder sudoku.jpg

    The input corresponding to the above configuration :

    ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
    A partially filled sudoku which is valid.

    Algorithm:
    Written By: Devesh Kumar
    Submission Details in Image: valid_sudoku.png
"""

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        row = [{} for i in range (9)]
        col = [{} for i in range (9)]
        box = [{} for i in range (9)]
        
        for i in range (9):
            for j in range (9):
                element = A[i][j]
                
                if element != ".":
                    if A[i][j] not in row [i]:
                        row[i][A[i][j]] = 1
                    else:
                        return 0
                    
                    if A[i][j] not in col [j]:
                        col[j][A[i][j]] = 1
                    else:
                        return 0
                        
                    boxNum = 3*(i/3)+(j/3)
                    if element not in box[boxNum]:
                        box[boxNum][element] = 1
                    else:
                        return 0
        return 1