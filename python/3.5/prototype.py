import copy
ori = "Hello!"
c1 = copy.copy(ori)
c2 = copy.deepcopy(ori)

print(c1)
print(c2)

import copy

class Product(object):
    def use(self, s):
        pass
    def createClone(self):
        pass

class Manager(object):
    __showcase = dict()
    def register(self, name, proto):
        self.__showcase[name] = proto
    def create(self, protoname):
        p = self.__showcase.get(protoname)
        return p.createClone()

class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar
    
    def use(self, s):
        length = len(s)
        deco = self.decochar * (length + 4 )
        print(deco)
        print(self.decochar,s,self.decochar)
        print(deco)
    
    def createClone(self):
        p = copy.deepcopy(self)
        return p

class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar
    
    def use(self, s):
        length = len(s)
        print('"%s"' %s)
        print(" %s " %(self.ulchar * length))
    
    def createClone(self):
        p = copy.deepcopy(self)
        return p


if __name__== "__main__":
    manager = Manager()
    upen = UnderlinePen("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)
    
    p1 = manager.create("strong message")
    p1.use("Hello, world.")
    p2 = manager.create("warning box")
    p2.use("Hello, world.")
    p3 = manager.create("slash box")
    p3.use("Hello, world.")

