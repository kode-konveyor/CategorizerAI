import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import TestHelper

optionPreparatorService = Autowired('optionPreparatorService')
config = Autowired('config')

class Test(unittest.TestCase):

    def setUp(self):
        with\
            Autowired('updateTestData', self, singleton=False),\
            MockedService('optionDisplayService', self):
            self.result = optionPreparatorService().prepareOptionsToOffer(
                self.updateTestData.rowNumber, self.updateTestData.data, self.updateTestData.categories)
    def test_prepareOptionsToOffer_returns_a_dict_keyed_by_small_numbers(self):
        self.assertEqual(self.updateTestData.resultKeys, list(self.result.keys()))

    def test_the_first_element_in_the_value_tuple_is_the_probability(self):
        self.assertEqual(self.updateTestData.data.problemValues[0][2], self.result[1][0])

    def test_the_second_element_in_the_value_tuple_is_a_value_of_the_categories_dict(self):
        self.assertEqual(self.updateTestData.categories[3], self.result[1][1])

    def test_prepareOptionsToOffer_displays_choice_key(self):
        TestHelper.assertCallParameter(self.updateTestData.resultKeys[0], self.optionDisplayService.displayOption, 0)

    def test_prepareOptionsToOffer_displays_probability(self):
        TestHelper.assertCallParameter(self.updateTestData.data.problemValues[0][2], self.optionDisplayService.displayOption, 1)

    def test_prepareOptionsToOffer_displays_categories(self):
        TestHelper.assertCallParameter(self.updateTestData.categories[3], self.optionDisplayService.displayOption, 2)

    def test_prepareOptionsToOffer_displays_all_offered_options(self):
        self.assertEqual(len(self.result.keys()),self.optionDisplayService.displayOption.call_count)

if __name__ == "__main__":
    unittest.main()