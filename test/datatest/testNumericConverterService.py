#coding=utf-8
import unittest
from categorizerai.winterboot.Autowired import Autowired
from datatest.DataTestData import DataTestData

numericConverterService = Autowired('numericConverterService')

class Test(unittest.TestCase):

    def setUp(self):
        self.testData = DataTestData()
        self.result = numericConverterService.createNumericArrayFromTextArray(
            self.testData.INPUT_ARRAY,self.testData.MAX_LENGTH)


    def test_createNumericArrayFromTextArray_creates_a_line_for_each_string(self):
        self.assertEqual( 3 , len(self.result))

    def test_createNumericArrayFromTextArray_creates_lines_of_max_length(self):
        self.assertEqual( self.testData.MAX_LENGTH, len(self.result[0]))

    def test_createNumericArrayFromTextArray_encodes_ascii_correctly(self):
        self.assertEqual( ord(self.testData.INPUT_ARRAY[0][0]) , self.result[0][0])

    def test_createNumericArrayFromTextArray_encodes_zero_after_string(self):
        self.assertEqual( 0 , self.result[1][3])

    def test_createNumericArrayFromTextArray_encodes_unicode_directly(self):
        self.assertEqual( ord(self.testData.INPUT_ARRAY[1][1]) , self.result[1][1])

    def test_createNumericArrayFromTextArray_encodes_the_whole_string(self):
        self.assertEqual( ord(self.testData.INPUT_ARRAY[2][3]) , self.result[2][3])


if __name__ == "__main__":
    unittest.main()