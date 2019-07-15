#coding=utf-8
import numpy
import pandas
from _io import StringIO
from Config import Config

class DataTestData:
    MAX_LENGTH = 6
    OUTPUT_NEURONS = 4
    INPUT_ARRAY = numpy.array([
        "abc",
        "cő",
        "efgh"   
           ])
    
    TRAIN_SET_DATA = """1\tblabla\t2
    2\tbeea\t3
    4\tbeaa\t3
    3\tbaz\t1"""
    PROBLEM_SET_DATA = """4\tboo
    5\tfefefe"""
    
    PROBLEM_OIDS=numpy.array([4,5])
    TRAIN_RESULTS=numpy.array([2,3,3,1,])
    config = Config()
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
    PROBLEM_MODEL_RESULT = [[ 0.4, 0, 0.6,   0],
                      [0, 0.3, 0, 0.7]]
    PROBLEM_ANSWERS = [(0.7, 3), (0.3, 1), (0, 0), (0, 2)]
    
