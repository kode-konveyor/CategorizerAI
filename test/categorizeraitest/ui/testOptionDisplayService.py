import unittest
from winterboot.Autowired import Autowired
import TestHelper

optionDisplayService = Autowired('optionDisplayService')

class Test(unittest.TestCase):

    def test_displayOption_displays_choice_number_probability_and_categories(self):
        with\
                Autowired('updateTestData', self),\
                unittest.mock.patch('sys.stdout') as mockedStdout:
            optionDisplayService().displayOption(self.updateTestData.resultKeys[0],
                                                    self.updateTestData.data.problemValues[0][2],
                                                    self.updateTestData.categories[3])
        TestHelper.assertPrintedOn(mockedStdout,self.updateTestData.outputOfFirstOption)

if __name__ == "__main__":
    unittest.main()