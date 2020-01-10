import unittest
from BubbleSort.BubbleSort import Bubblesort


class BubbleSort_test(unittest.TestCase):

    def test_Bubblesort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]

        expected1=([11, 12, 22, 25, 34, 64, 90])

        result1 = Bubblesort.bubbleSort(arr)
        self.assertEqual(result1, expected1)


if __name__ == '__main__':
    unittest.main()