# lst = [i for i in range(5)]
# lst = [output_exp for var in input_list]
# print(lst)

# newlist = [i*i for i in range(1,5) if i!=2]
# print(newlist)
# newlist = [5,10,15,20]

# newlist=[]
# for i in range(1,5):
#     if i!=2:
#         newlist.append(i*i)
# print(newlist)

# mydict = {i:f'ID100{i}' for i in range(1,5)}
# print(mydict)


newlist = {i*i for i in range(1,5)}
print(newlist)