from categorizerai.springboot.Service import Service

@Service
class ExampleService(object):
    def method(self, arg):
        return "got:"+arg
