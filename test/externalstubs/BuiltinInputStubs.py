from winterboot.TestDataForStub import TestDataForStub
from winterboot.Stubs import Stubs

@Stubs('categorizerai.ui.ChoiceAskService.input')
class BuiltinInputStubs:
    def behaviour(self,service):
        with TestDataForStub('UiTestData') as UiTestData:
            service.return_value = UiTestData.ANSWER_TO_CHOICE_PROMPT
