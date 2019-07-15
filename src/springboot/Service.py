from springboot.SpringBoot import providers

class Service(object):
    def __init__(self, klass):
        className = klass.__name__
        serviceId = className[0].lower() + className[1:]
        if serviceId not in providers:
            providers[serviceId] = []
        providers[serviceId].append(klass)
        self.wrapped = klass
    def __call__(self):
        return self.wrapped()

