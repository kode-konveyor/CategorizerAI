import unittest
from categorizerai.winterboot.Autowired import Autowired
from updatetest.UpdateTestData import UpdateTestData
import TestHelper

optionDisplayService = Autowired('optionDisplayService')

class Test(unittest.TestCase):

    def test_displayOption_displays_choice_number_probability_and_categories(self):
        self.testData = UpdateTestData()
        with unittest.mock.patch('sys.stdout') as mockedStdout:
            optionDisplayService.displayOption(self.testData.resultKeys[0],
                                                    self.testData.data.problemValues[0][2],
                                                    self.testData.categories[3])
        TestHelper.assertPrintedOn(mockedStdout,self.testData.outputOfFirstOption)

if __name__ == "__main__":
    unittest.main()