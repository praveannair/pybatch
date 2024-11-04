class Emp():
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def intro(self):
        print(f"Hello {self.name}")
       
class Freelance(Emp):
    def __init__(self, id, name, addr):
        super().__init__(id, name)
        self.addr = addr
    
    def intro(self):
        print(f"Hello! I am {self.name} and I am from {self.addr}")

newemp = Freelance(101, "Ria", "Delhi")
newemp.intro()
# newemp.intro1()

newemp1 = Emp(101,"Cathy")
newemp1.intro()


# newemp1.intro()














# print(newemp.id,newemp.name,newemp.addr)