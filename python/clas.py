class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting!" ) 
    
    def down(self):
        print(self.name.title()+" is now down!")


my_dogo = Dog('luis', 3)

my_dogo.down()
my_dogo.sit()
