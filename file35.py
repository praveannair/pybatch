class MyClass:
  x = 5 #class attribute or variable
  def sayHello(self):
    print("Hello")
    print(self.x) # to access class variable
  def greet(self):
    print("Good Morning")
    
class MyClass1:
  x = 5 #class attribute or variable
  def sayHello(self):
    print("Hello")
    print(self.x) # to access class variable
  def greet(self):
    print("Good Evening")


obj1 = MyClass1()
obj1.greet()

obj2 = MyClass()
obj2.greet()



# p1 = MyClass()
# print(p1.x)
# p1.sayHello()
# p1.greet()



# x=5
# def sayHello():
#     print("Hello")
#     print(x)
# def greet():
#     print("Good Morning")
    
# sayHello()
# greet()