from winterboot.TestDataForStub import TestDataForStub
from winterboot.Stubs import Stubs

@Stubs('categorizerai.ui.ChoiceAskService.input')
class BuiltinInputStubs:
    def behaviour(self,service):
        with TestDataForStub('uiTestData') as uiTestData:
            service.return_value = uiTestData.ANSWER_TO_CHOICE_PROMPT
