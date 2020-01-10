import unittest
from BMI.BMI import BMICALC


class BMI_test(unittest.TestCase):

    def test_underweight_BMI(self):
        weight = 50
        height = 1.70

        expected1='Your BMI is',17.301038062283737, 'which means you are underweight.'

        result1 = BMICALC.BMI(height,weight)
        self.assertEqual(result1, expected1)

    def test_proper_BMI(self):
        weight = 70
        height = 1.70

        expected2='Your BMI is', 24.221453287197235, 'which means you are normal.'
        result2= BMICALC.BMI(height,weight)
        self.assertEqual(result2,expected2)

    def test_overweight_BMI(self):
        weight = 75
        height = 1.70
        expected3 = 'Your BMI is', 25.95155709342561, 'which means you are overweight.'

        result3 = BMICALC.BMI(height, weight)

        self.assertEqual(result3, expected3)

    def test_obese_BMI(self):
        weight = 90
        height = 1.70

        expected4 = 'Your BMI is',31.14186851211073, 'which means you are obese.'

        result4 = BMICALC.BMI(height, weight)
        self.assertEqual(result4, expected4)

if __name__ == '__main__':
    unittest.main()