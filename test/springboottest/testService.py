
import unittest
from springboot.SpringBoot import providers
from springboottest.ExampleService import ExampleService


class Test(unittest.TestCase):

    def test_Service_annotation_puts_the_service_to_the_providers_list_for_the_service_id(self):
        providerList = providers['exampleService']
        self.assertEquals(ExampleService.wrapped, providerList[0])  # @UndefinedVariable


if __name__ == "__main__":
    unittest.main()