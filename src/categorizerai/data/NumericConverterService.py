import numpy
from winterboot.Service import Service
from categorizerai.types.NdArray import NdArray


@Service
class NumericConverterService:

    def call(self,inputSet: NdArray[str], max_length:int) -> NdArray[NdArray[float]]:
        whole = numpy.ndarray((inputSet.shape[0],max_length))
        for i in range(inputSet.shape[0]):
            for j in range(max_length):
                if(j<len(inputSet[i])):
                    whole[i][j] = ord(inputSet[i][j])
                else:
                    whole[i][j]=0
        return whole
