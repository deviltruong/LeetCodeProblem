"""
529. Minesweeper
https://leetcode.com/problems/minesweeper/

"""

class Solution:
    def updateBoard(self, board, click):
        (row, col) = click
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                nMine = 0
                for r, c in directions:
                    if 0 <= row+r < len(board) and 0 <= col+c < len(board[0]):
                        if board[row + r][col + c] == 'M':
                            nMine += 1
                if nMine == 0:
                    board[row][col] = 'B'
                    # update around square
                    for r_a, c_a in directions:
                        self.updateBoard(board, [row + r_a, col + c_a])
                else:
                    board[row][col] = str(nMine)

        return board

if __name__ == "__main__":
    s = Solution()
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3,0]
    expected = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    print(s.updateBoard(board, click) == expected)