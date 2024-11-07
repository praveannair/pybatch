def my_gen():
    n=1
    # print("This is printed first")
    yield n
    n=n+1
    # print("This is printed second")
    yield n

   
for item in my_gen():
    print(item)
