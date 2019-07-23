#coding=utf-8
import unittest
from winterboot.Autowired import Autowired

numericConverterService = Autowired('NumericConverterService')

class Test(unittest.TestCase):

    def setUp(self):
        with Autowired('DataTestData',self, singleton=False):
            self.result = numericConverterService.call(
                self.DataTestData.TRAIN_SET_VALUES,self.DataTestData.MAX_LENGTH)

    def test_createNumericArrayFromTextArray_creates_a_line_for_each_string(self):
        self.assertEqual( len(self.DataTestData.TRAIN_SET_VALUES) , len(self.result))

    def test_createNumericArrayFromTextArray_creates_lines_of_max_length(self):
        self.assertEqual( self.DataTestData.MAX_LENGTH, len(self.result[0]))

    def test_createNumericArrayFromTextArray_encodes_ascii_correctly(self):
        self.assertEqual( ord(self.DataTestData.TRAIN_SET_VALUES[0][0]) , self.result[0][0])

    def test_createNumericArrayFromTextArray_encodes_zero_after_string(self):
        self.assertEqual( 0 , self.result[1][3])

    def test_createNumericArrayFromTextArray_encodes_unicode_directly(self):
        self.assertEqual( ord(self.DataTestData.TRAIN_SET_VALUES[1][1]) , self.result[1][1])

    def test_createNumericArrayFromTextArray_encodes_the_whole_string(self):
        self.assertEqual( ord(self.DataTestData.TRAIN_SET_VALUES[2][3]) , self.result[2][3])


if __name__ == "__main__":
    unittest.main()