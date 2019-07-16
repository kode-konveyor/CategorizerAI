import unittest
from winterboot.WinterBoot import consumers
from winterboot.Autowired import Autowired

class Test(unittest.TestCase):


    def setUp(self):
        self.serviceId = 'exampleService'
        self.testArtifact = Autowired(self.serviceId)

    def testAutowired_stores_itself_in_the_consumers_for_service_id(self):
        self.assertTrue(self.testArtifact in consumers[self.serviceId])

if __name__ == "__main__":
    unittest.main()