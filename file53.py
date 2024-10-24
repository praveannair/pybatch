def f1(x):
    def wrapper():
        print("f2 begins")
        x()
        print("f2 ends")
    return wrapper

@f1
def f2():
    print("I am f2")

f2()

