import unittest
from springboot.Autowired import Autowired
from aitest import AiTestHelper

prepareDataService = Autowired("prepareDataService")

class Test(unittest.TestCase):

    def testName(self):
        result = prepareDataService.prepareData(AiTestHelper.TRAIN_VALUES, AiTestHelper.TRAIN_RESULTS)


if __name__ == "__main__":
    unittest.main()