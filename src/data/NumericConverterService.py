import numpy
from springboot.Service import Service

@Service
class NumericConverterService:

    def num(self,s):
        try:
            return int(s)
        except ValueError:
            return None

    def createNumericArrayFromTextArray(self,inputSet, max_length):
        whole = numpy.ndarray((inputSet.shape[0],max_length))
        for i in range(inputSet.shape[0]):
            for j in range(max_length):
                if(j<len(inputSet[i])):
                    whole[i][j] = ord(inputSet[i][j])
                else:
                    whole[i][j]=0
        return whole
