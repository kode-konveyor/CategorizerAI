from winterboot.TestData import TestData

@TestData
class UiTestData(object):

    def __init__(self):
        self.ACCURACY_ERROR_MESSAGE = "Accuracy is too small, exiting. Try again."
        self.PROMPT = "choice: "
        self.ANSWER_TO_CHOICE_PROMPT = "42"
        self.ACCURACY_STRING = "accuracy:{0}"

