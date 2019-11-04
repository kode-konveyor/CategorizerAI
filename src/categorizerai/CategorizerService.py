#!/usr/bin/python3
#coding=utf-8
import pandas
from winterboot.Autowired import Autowired
from winterboot.Service import Service

config = Autowired('Config')()
prepareDataService = Autowired('PrepareDataService')
neuralNetBuilderService = Autowired('NeuralNetBuilderService')
neuralNetTrainerService = Autowired('NeuralNetTrainerService')
accuracyCheckService = Autowired('AccuracyCheckService')
updateService = Autowired('UpdateService')

@Service
class CategorizerService(object):
    def call(self) -> None:
        trainSet = pandas.read_csv(config.TRAINING_SET_FILE,'\t',encoding='utf-8',names=config.TRAINING_SET_COLUMNS)
        problemSet = pandas.read_csv(config.PROBLEM_SET_FILE,'\t',encoding='utf-8',names=config.PROBLEM_SET_COLUMNS)
        
        data = prepareDataService.call(trainSet, problemSet)
        model = neuralNetBuilderService.call(data.max_length, data.numberOfOutputNeurons)
        accuracy = neuralNetTrainerService.call(data.trainValues, data.trainResults, model)
        accuracyCheckService.call(accuracy)
        data.problemResults=model.predict(data.problemValues)
        
        updateService.call(data)

