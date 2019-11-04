import unittest
from winterboot.Autowired import Autowired
import TestHelper

optionDisplayService = Autowired('OptionDisplayService')

class Test(unittest.TestCase):

    def test_displayOption_displays_choice_number_probability_and_categories(self):
        with\
                Autowired('UpdateTestData', self),\
                unittest.mock.patch('sys.stdout') as mockedStdout:
            optionDisplayService.call(self.UpdateTestData.resultKeys[0],
                                                    self.UpdateTestData.data.problemValues[0][2],
                                                    self.UpdateTestData.categories[3])
        TestHelper.assertPrintedOn(mockedStdout,self.UpdateTestData.outputOfFirstOption)

if __name__ == "__main__":
    unittest.main()