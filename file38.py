class Mammal:
  def walk(self):
    print("walking...")
    
class Dog(Mammal):
  def bark(self):
    print("barking...")

d = Dog()
d.bark()
d.walk()



# d.walk() # inherited from Mammal
# d.bark() # defined in Dog



# class Dog():
#   def walk(self):
#       print("walking...")
#   def bark(self):
#     print("barking...")
# d = Dog()
# d.walk()

# class Horse():
#   def walk(self):
#       print("walking...")
#   def bark(self):
#     print("barking...")

# h = Horse()
# h.walk()
