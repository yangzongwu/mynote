from unittest import TestCase
from available_Captures_for_Rook import Solution

class TestSolution(TestCase):
    def test_numRookCaptures(self):
        test = Solution()
        A=[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],
           [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
           [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        self.assertEqual(3,test.numRookCaptures(A))
        B=[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],
           [".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],
           [".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        self.assertEqual(0,test.numRookCaptures(B))


if __name__ == '__main__':
    unittest.main()
