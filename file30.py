#Positional Argument,unnamed
# def add(a,b):
#     print(a+b)

# add(4,5)

#Keyword/named argument
# def add(a,b):
#     print(a+b)

# add(b=5,a=6)

# def add(a,b):
#     print(a+b)

# add(4,b=5)

# def add(a,b):
#     print(a+b)

# add(b=5,4)


# def add(a,b,c,d):
#     print(a+b+c+d)

# add(4,2,c=5,d=6)



# def add(a=0,b=0):
#     print(a+b)

# # add(4,2)
# add(6,7)

# def add(*args):
#     print(args[0])

# add(4,5,6,7,8,9)


def add(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

add(a=4,b=6,c=1,d=5,r=4,q=2)
