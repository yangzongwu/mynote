from unittest import TestCase
from MIT算法导论.Coding.InsertionSort.insertion_sort import insertion_sort
from MIT算法导论.Coding.InsertionSort.insertion_sort import insert_sorted_num

class TestInsertion_sort(TestCase):
    def test_insertion_sort_1(self):
        after_sort = insertion_sort([1, 2, 3, 4, 5, 6])
        self.assertEqual(after_sort, [1, 2, 3, 4, 5, 6])

    def test_insertion_sort_2(self):
        after_sort = insertion_sort([])
        self.assertEqual(after_sort, [])

    def test_insertion_sort_3(self):
        after_sort = insertion_sort([1])
        self.assertEqual(after_sort, [1])

    def test_insertion_sort_4(self):
        after_sort = insertion_sort([6,5,4,3,2,1])
        self.assertEqual(after_sort, [1, 2, 3, 4, 5, 6])

    def test_insertion_sort_5(self):
        after_sort = insertion_sort([1,2,4,5,3,6,8,12])
        self.assertEqual(after_sort, [1,2,3,4,5,6,8,12])



    def test_insert_sorted_num(self):
        exp=insert_sorted_num([],1)
        self.assertEqual(exp,[1])

    def test_insert_sorted_num_1(self):
        exp = insert_sorted_num([1, 2], 3)
        self.assertEqual(exp, [1, 2, 3])

    def test_insert_sorted_num_2(self):
        exp = insert_sorted_num([1,3], 2)
        self.assertEqual(exp, [1, 2, 3])

    def test_insert_sorted_num_3(self):
        exp=insert_sorted_num([2,3],1)
        self.assertEqual(exp,[1,2,3])