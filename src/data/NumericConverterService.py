import numpy
from springboot.Service import Service

@Service
class NumericConverterService:

    def num(self,s):
        try:
            return int(s)
        except ValueError:
            return None

    def createNumericArrayFromTextArray(self,x_train, max_length):
        whole = numpy.ndarray((x_train.shape[0],max_length))
        for i in range(x_train.shape[0]):
            for j in range(max_length):
                if(j<len(x_train[i])):
                    whole[i][j] = ord(x_train[i][j])
                else:
                    whole[i][j]=0
        return whole
