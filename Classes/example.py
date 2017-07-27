class Class1:
    def __init__(self, test_attribute):
        self.test_attribute = test_attribute


class Class2:
    def __init__(self, test_attribute):
        self.test_attribute = 10


class Class3:
    def __init__(self, test_attribute=50):
        self.test_attribute = test_attribute

test_object1 = Class1(20)
print 'Class1', test_object1.test_attribute

test_object2 = Class2(20)
print 'Class2', test_object2.test_attribute

test_object3 = Class3(20)
print 'Class3 with a value', test_object3.test_attribute

test_object3 = Class3()
print 'Class3 without a value', test_object3.test_attribute
