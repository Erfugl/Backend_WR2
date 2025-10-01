#Classes
class Person:
  def __init__(self,name,age): 
    self.name = name
    self.age = age
  
  def greet(self):
    print(f"Greetings {self.name}, you are {self.age} years old!")

class Student(Person):
  def __init__(self,name,age,student_id):
    self.name = name
    self.age = age
    self.student_id = student_id