class Person:
  def __init__(self, name, age):
    self.name = name #instance attribute of variable
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
  def chkMinor(self):
    if self.age < 18:
        print("Minor")
    else:
        print("Adult")
    
p1 = Person("Peter", 14)

p1.myfunc()
p1.chkMinor()