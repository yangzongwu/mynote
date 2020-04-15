from unittest import TestCase
from MIT算法导论.Coding.MergeSort.merge_sort import merge_sort


class TestMergeSort(TestCase):
    def test_merge_sort(self):
        exp = merge_sort([1, 3, 6, 2, 4, 8])
        self.assertEqual(exp, [1, 2, 3, 4, 6, 8])

    def test_merge_sort_1(self):
        exp = merge_sort([])
        self.assertEqual(exp, [])

    def test_merge_sort_2(self):
        exp = merge_sort([2])
        self.assertEqual(exp, [2])

    def test_merge_sort_3(self):
        exp = merge_sort([3,2,1])
        self.assertEqual(exp, [1,2,3])