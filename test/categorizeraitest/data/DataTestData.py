#coding=utf-8
import numpy
import pandas

from winterboot.Autowired import Autowired
from winterboot.TestData import TestData

@TestData
class DataTestData:
    def __init__(self):
        with\
            Autowired('dbTestData', singleton=False) as dbTestData,\
            Autowired('config', singleton=False) as config:
                self.TRAIN_SET_VALUES = numpy.array(list(dbTestData.trainComments))
                self.PROBLEM_OIDS=numpy.array(list(dbTestData.problemOids))
                self.TRAIN_SET=pandas.read_csv(config.TRAINING_SET_FILE,'\t',encoding='utf-8',names=config.TRAINING_SET_COLUMNS)
                self.PROBLEM_SET=pandas.read_csv(config.PROBLEM_SET_FILE,'\t',encoding='utf-8',names=config.PROBLEM_SET_COLUMNS)
              
                self.PROBLEM_SET_VALUES = numpy.array(list(dbTestData.problemComments))
                self.MAX_LENGTH = 6
                self.OUTPUT_NEURONS = 4
                self.TRAIN_RESULTS=numpy.array([2,3,3,1,])
                self.PROBLEM_MODEL_INPUT = [[ 98, 111, 111,   0,   0,   0],
                                  [102, 101, 102, 101, 102, 101]]
                self.TRAIN_MODEL_INPUT = [[ 98, 108,  97,  98, 108,  97],
                                 [ 98, 101, 101,  97,   0,   0],
                                 [ 98, 101,  97,  97,   0,   0],
                                 [ 98,  97, 122,   0,   0,   0]]
                self.PROBLEM_MODEL_RESULT = [[ 0.3, 0.1, 0.6,   0],
                                  [0, 0.3, 0.1, 0.6]]
