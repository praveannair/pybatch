name = input("Enter your name:")
# print(name)
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[-2])


# ch = name[0]
# if ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u":
#     print("Invalid Input")
# else:
#     print("First letter is a vowel")
counter=0
for ch in name.lower():
    ch1 = name[0]
    if ch1!="a" and ch1!="e" and ch1!="i" and ch1!="o" and ch1!="u":
        print("Invalid Input")
        break
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        counter=counter+1
else:
    if counter==1:
        print(f"There is a vowel in the name {name}.")
    elif counter>1:
        print(f"There are {counter} vowels in the name {name}.")
    else:
        print(f"No vowels found in the name {name}.")

