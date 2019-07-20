from winterboot.Autowired import Autowired

def behaviour(updateTestData):
        prepareDataService = Autowired('prepareDataService')()
        prepareDataService.prepareData.return_value = updateTestData.data