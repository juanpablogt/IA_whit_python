class NER():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def op(self):

        print(self.age+3)

ner = NER('luus', 1)
ner.op()