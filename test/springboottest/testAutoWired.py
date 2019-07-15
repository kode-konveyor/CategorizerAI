import unittest
from springboot.SpringBoot import consumers
from springboot.Autowired import Autowired


class Test(unittest.TestCase):


    def setUp(self):
        self.serviceId = 'exampleService'
        self.testArtifact = Autowired(self.serviceId)

    def testAutowired_stores_itself_in_the_consumers_for_service_id(self):
        self.assertTrue(self.testArtifact in consumers[self.serviceId])

    def test_wire_wires_autowired_objects(self):
        Autowired.wire()
        self.assertEqual("got:foo", self.testArtifact.method("foo"))

if __name__ == "__main__":
    unittest.main()