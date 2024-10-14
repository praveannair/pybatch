x="global"
def g():
    x="enclosing"
    def e():
        x="local"
        print(x)
    e()
    print(x)
g()
print(x)
