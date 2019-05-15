class Person:
    def __init__(self,name): # Constructor of the class
        self.name=name
    def designation(self): #Abstract method
        raise NotImplementedError ("Subclass must implement abstract method")
class Employee(Person):
    def designation(self):
        return 'Software Engineer'
class Doctor(Person):
    def designation(self):
        return 'Cardiologist'
class Student(Person):
    def designation(self):
        return 'Graduate Engineer'
persons=[Employee('Guido Van Rossum'),Doctor('Aggarwal'),Student('Aarav')]
for person in persons:
    print (person.name+':'+person.designation())
    
