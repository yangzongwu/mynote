import unittest
from find_the_Town_Judge import Solution

class MyTestCase(unittest.TestCase):
    def test_findJudge(self):
        Test=Solution()
        self.assertEqual(2,Test.findJudge(2,[[1,2]]))
        self.assertEqual(3, Test.findJudge(3,[[1,3],[2,3]]))
        self.assertEqual(-1, Test.findJudge(3,[[1,3],[2,3],[3,1]]))
        self.assertEqual(-1, Test.findJudge(3,[[1,2],[2,3]]))
        self.assertEqual(3, Test.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))

if __name__ == '__main__':
    unittest.main()
