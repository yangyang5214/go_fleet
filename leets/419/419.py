class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r = 0

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):

                # 先给后取
                if board[i][j] == 'X':
                    r = r + 1
                    if i > 0 and board[i - 1][j] == 'X':
                        r -= 1
                    if j > 0 and board[i][j - 1] == 'X':
                        r -= 1
        return r


if __name__ == '__main__':
    s = Solution()
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    print(s.countBattleships(board))
