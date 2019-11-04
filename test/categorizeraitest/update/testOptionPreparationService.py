import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

optionPreparatorService = Autowired('OptionPreparatorService')

class Test(unittest.TestCase):

    def setUp(self):
        with\
            Autowired('UpdateTestData', self, singleton=False),\
            MockedService('OptionDisplayService', self):
            self.result = optionPreparatorService.call(
                self.UpdateTestData.rowNumber, self.UpdateTestData.data, self.UpdateTestData.categories)
    def test_prepareOptionsToOffer_returns_a_dict_keyed_by_small_numbers(self):
        self.assertEqual(self.UpdateTestData.resultKeys, list(self.result.keys()))

    def test_the_first_element_in_the_value_tuple_is_the_probability(self):
        self.assertEqual(self.UpdateTestData.data.problemValues[0][2], self.result[1][0])

    def test_the_second_element_in_the_value_tuple_is_a_value_of_the_categories_dict(self):
        self.assertEqual(self.UpdateTestData.categories[3], self.result[1][1])

    def test_prepareOptionsToOffer_displays_choice_key(self):
        TestHelper.assertCallParameter(self.UpdateTestData.resultKeys[0], self.OptionDisplayService.call, 0)

    def test_prepareOptionsToOffer_displays_probability(self):
        TestHelper.assertCallParameter(self.UpdateTestData.data.problemValues[0][2], self.OptionDisplayService.call, 1)

    def test_prepareOptionsToOffer_displays_categories(self):
        TestHelper.assertCallParameter(self.UpdateTestData.categories[3], self.OptionDisplayService.call, 2)

    def test_prepareOptionsToOffer_displays_all_offered_options(self):
        self.assertEqual(len(self.result.keys()),self.OptionDisplayService.call.call_count)

if __name__ == "__main__":
    unittest.main()