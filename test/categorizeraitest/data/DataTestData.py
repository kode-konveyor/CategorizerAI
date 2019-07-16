#coding=utf-8
import numpy
import pandas
from _io import StringIO
from categorizeraitest.Config import Config

class DataTestData:
    MAX_LENGTH = 6
    OUTPUT_NEURONS = 4
    INPUT_ARRAY = numpy.array([
        "abc",
        "cő",
        "efgh"   
           ])
    
    PROBLEM_OIDS=numpy.array([4,5])
    TRAIN_RESULTS=numpy.array([2,3,3,1,])
    config = Config()
    TRAIN_SET_DATA = config.TRAIN_SET_DATA
    PROBLEM_SET_DATA = config.PROBLEM_SET_DATA
    TRAIN_SET=pandas.read_csv(StringIO(TRAIN_SET_DATA),'\t',names=config.TRAINING_SET_COLUMNS)
    PROBLEM_SET=pandas.read_csv(StringIO(PROBLEM_SET_DATA),'\t',names=config.TRAINING_SET_COLUMNS)
    
    TRAIN_SET_VALUES = numpy.array(['blabla', 'beea', 'beaa', 'baz'])
    PROBLEM_SET_VALUES = numpy.array(['boo', 'fefefe'])
    PROBLEM_MODEL_INPUT = [[ 98, 111, 111,   0,   0,   0],
                      [102, 101, 102, 101, 102, 101]]
    TRAIN_MODEL_INPUT = [[ 98, 108,  97,  98, 108,  97],
                     [ 98, 101, 101,  97,   0,   0],
                     [ 98, 101,  97,  97,   0,   0],
                     [ 98,  97, 122,   0,   0,   0]]
    PROBLEM_MODEL_RESULT = [[ 0.3, 0.1, 0.6,   0],
                      [0, 0.3, 0.1, 0.6]]

    
