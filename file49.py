# test=[True,True,False,True]
# print(all(test))
# print(any(test))


score = [39,45,7,86]
result = [i>30 for i in score]
flag = all(result)
if flag==True:
    print("Pass")
else:
    print("Fail")


# flag="Fail"
# for i in score:
#     if i<30:
#         break
# else:
#     flag="pass"
    
# print(flag)
