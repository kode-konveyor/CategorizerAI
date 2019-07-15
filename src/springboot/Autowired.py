from springboot.SpringBoot import consumers, providers

class Autowired(object):
    def __init__(self, moduleName):
        if moduleName not in consumers:
            consumers[moduleName] = []
        consumers[moduleName].append(self)
        
    def __getattribute__(self, name):
        if name in ['provider', '__getattribute__']:
            return object.__getattribute__(self,name)
        return getattr(self.provider, name)
    

    @staticmethod
    def wire():
        for serviceId in consumers:
            provider = providers[serviceId][0]
            if type(provider) == type:
                provider = provider()
            providers[serviceId][0] = provider
            for consumer in consumers[serviceId]:
                consumer.provider = provider
