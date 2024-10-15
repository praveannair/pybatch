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
