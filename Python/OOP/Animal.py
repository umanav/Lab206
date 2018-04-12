class Animal(object):
    def __init__(self, name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def disp_health(self):
        print "the health of",self.name,"is",self.health
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name,150)
    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name,170)
    def fly(self):
        self.health -= 10
        return self
    def disp_health(self):
        super(Dragon,self).disp_health()
        print "I am a Dragon"
        return self


animal1 = Animal("shark",100)
animal1.walk().walk().walk().run().run().disp_health()
dog1 = Dog("spot")
dog1.walk().walk().walk().run().run().pet().disp_health()
dragon1 = Dragon("chuck")
dragon1.walk().walk().fly().fly().run().disp_health()
