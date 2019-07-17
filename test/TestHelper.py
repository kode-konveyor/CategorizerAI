import unittest

asserter = unittest.TestCase()
def assertPrintedOn(mockedStdout, printedObject):
    argsList = mockedStdout.write.call_args_list
    asserter.assertEqual(str(printedObject), argsList[0][0][0])
    asserter.assertEqual('\n', argsList[1][0][0])
    asserter.assertEqual(2, len(argsList))



def callArguments(functionMock, callNumber=0):
    funcArgsForCall = functionMock.call_args_list[callNumber][0]
    return funcArgsForCall

def callArgument(functionMock, argPosition, callNumber=0):
    funcArgsForCall = callArguments(functionMock, callNumber)
    functionArgument = funcArgsForCall[argPosition]
    return functionArgument

def callKwArgument(functionMock, callNumber=0):
    return functionMock.call_args_list[callNumber][1]

def assertCallParameter(expected, functionMock, argPosition, callNumber=0, prepareForCheck= lambda x: x):
    functionArgument = callArgument(functionMock, argPosition, callNumber)
    asserter.assertEqual(prepareForCheck(expected), prepareForCheck(functionArgument))

def assertIterablesEqual(expectedIterable, actualIterable):
    return asserter.assertEqual(list(expectedIterable), 
        list(actualIterable))

def assertFunctionParametersAcrossAllcalls(expectedIterable, functionMock, position):
    assertIterablesEqual(
        expectedIterable,
        map(
            lambda x:functionMock.call_args_list[x][position][position],
            range(len(functionMock.call_args_list))))
