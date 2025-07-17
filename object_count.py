class ObjectCount:
    count = 0

    def __init__(self):
        ObjectCount.count += 1 

    @classmethod
    def get_count(cls):
        return cls.count


obj1 = ObjectCount()
obj2 = ObjectCount()   
obj3 = ObjectCount()    
print(obj2.get_count())     


