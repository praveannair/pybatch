class Emp():
    def __init__(self, id, name):
        self.id = id
        self.name = name
       
class Freelance(Emp):
    def __init__(self, id, name, addr):
        super().__init__(id, name)
        self.addr = addr
    
    def intro(self):
        print(f"Hello! I am {self.name} and I am from {self.addr}")

newemp = Freelance(101, "Ria", "Delhi")
newemp.intro()


# print(newemp.id,newemp.name,newemp.addr)