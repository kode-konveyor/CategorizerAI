#coding=utf-8
import unittest
from springboot.Autowired import Autowired
from datatest import DataTestHelper

numericConverterService = Autowired('numericConverterService')


class Test(unittest.TestCase):

    def setUp(self):
        Autowired.wire()
        self.result = numericConverterService.createNumericArrayFromTextArray(
            DataTestHelper.INPUT_ARRAY,DataTestHelper.MAX_LENGTH)

    def test_integer_is_interpreted_correctly_by_num(self):
        self.assertEqual( 3 , numericConverterService.num("3"))

    def test_noninteger_is_interpreted_correctly_by_num(self):
        self.assertEqual( None , numericConverterService.num("foo"))

    def test_createNumericArrayFromTextArray_creates_a_line_for_each_string(self):
        self.assertEqual( 3 , len(self.result))

    def test_createNumericArrayFromTextArray_creates_lines_of_max_length(self):
        self.assertEqual( DataTestHelper.MAX_LENGTH , len(self.result[0]))

    def test_createNumericArrayFromTextArray_encodes_ascii_correctly(self):
        self.assertEqual( 97 , self.result[0][0])

    def test_createNumericArrayFromTextArray_encodes_zero_after_string(self):
        self.assertEqual( 0 , self.result[1][3])

    def test_createNumericArrayFromTextArray_encodes_unicode_directly(self):
        self.assertEqual( 337 , self.result[1][1])

    def test_createNumericArrayFromTextArray_encodes_the_whole_string(self):
        self.assertEqual( 104 , self.result[2][3])


if __name__ == "__main__":
    unittest.main()