#coding=utf-8
import numpy
import pandas

from categorizeraitest.Config import Config
from categorizeraitest.db.DbTestData import DbTestData

class DataTestData:
    dbTestData = DbTestData()
    MAX_LENGTH = 6
    OUTPUT_NEURONS = 4
    TRAIN_SET_VALUES = numpy.array(list(dbTestData.trainComments))
    PROBLEM_OIDS=numpy.array(list(dbTestData.problemOids))
    TRAIN_RESULTS=numpy.array([2,3,3,1,])
    config = Config()
    TRAIN_SET=pandas.read_csv(config.TRAINING_SET_FILE,'\t',encoding='utf-8',names=config.TRAINING_SET_COLUMNS)
    PROBLEM_SET=pandas.read_csv(config.PROBLEM_SET_FILE,'\t',encoding='utf-8',names=config.PROBLEM_SET_COLUMNS)
  
    PROBLEM_SET_VALUES = numpy.array(list(dbTestData.problemComments))
    PROBLEM_MODEL_INPUT = [[ 98, 111, 111,   0,   0,   0],
                      [102, 101, 102, 101, 102, 101]]
    TRAIN_MODEL_INPUT = [[ 98, 108,  97,  98, 108,  97],
                     [ 98, 101, 101,  97,   0,   0],
                     [ 98, 101,  97,  97,   0,   0],
                     [ 98,  97, 122,   0,   0,   0]]
    PROBLEM_MODEL_RESULT = [[ 0.3, 0.1, 0.6,   0],
                      [0, 0.3, 0.1, 0.6]]
