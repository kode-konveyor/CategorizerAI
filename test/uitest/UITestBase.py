import unittest

class UITestBase(unittest.TestCase):


    def assertPrintedOn(self, mockedStdout, printedObject):
        argsList = mockedStdout.write.call_args_list
        self.assertEqual(str(printedObject), argsList[0][0][0])
        self.assertEqual('\n', argsList[1][0][0])
        self.assertEqual(2, len(argsList))

if __name__ == "__main__":
    unittest.main()