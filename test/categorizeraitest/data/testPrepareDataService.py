import unittest
from winterboot.Autowired import Autowired
from winterboot.MockedService import MockedService
import numpy

prepareDataService = Autowired("PrepareDataService")

class Test(unittest.TestCase):

    def setUp(self):
        with\
                Autowired('DataTestData',self),\
                MockedService('NumericConverterService', self):
            self.result = prepareDataService.call(self.DataTestData.TRAIN_SET, self.DataTestData.PROBLEM_SET)
        self.callList = self.NumericConverterService.call.mock_calls

    def test_number_of_output_neurons_are_calculated(self):
        self.assertEqual(self.DataTestData.OUTPUT_NEURONS, self.result.numberOfOutputNeurons)

    def test_problem_oids_is_the_list_of_oids_from_problemSet(self):
        self.assertTrue(numpy.array_equal(self.DataTestData.PROBLEM_OIDS,self.result.problemOids))

    def test_train_results_is_the_list_of_results_from_trainSet(self):
        self.assertTrue(numpy.array_equal(self.DataTestData.TRAIN_RESULTS, self.result.trainResults))

    def test_trainValues_are_calculated_using_NumericConverterService(self):
        self.assertEqual("firstValue",self.result.trainValues)

    def test_max_length_is_calculated_as_the_max_string_length_in_both_sets(self):
        self.assertEqual(self.DataTestData.MAX_LENGTH,self.result.max_length)

    def test_problemValues_are_calculated_using_NumericConverterService(self):
        self.assertEqual("secondValue",self.result.problemValues)

    def test_trainValues_are_calculated_from_the_values_of_trainSet(self):
        self.assertTrue(numpy.array_equal(self.DataTestData.TRAIN_SET_VALUES,self.callList[0][1][0]))

    def test_trainValues_calculation_uses_the_maximal_string_length_of_all_values_in_the_train_set_and_problem_set(self):
        self.assertEqual(self.DataTestData.MAX_LENGTH,self.callList[0][1][1])

    def test_problemValues_are_calculated_from_the_values_of_problemSet(self):
        self.assertTrue(numpy.array_equal(self.DataTestData.PROBLEM_SET_VALUES,self.callList[1][1][0]))

    def test_problemValues_calculation_uses_the_maximal_string_length_of_all_values_in_the_train_set_and_problem_set(self):
        self.assertEqual(self.DataTestData.MAX_LENGTH,self.callList[1][1][1])

if __name__ == "__main__":
    unittest.main()