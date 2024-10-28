# import re
# str = 'john@gmail.com'
# pattern ='@'
# flag = '@' in str
# if flag==True:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# str = 'johngmail.com'
# pattern ='@'
# i=len(str)-1
# while i>=0:
#     if pattern==str[i]:
#         print('Valid Email')
#         break
#     else:
#         i=i-1
# else:
#     print("Invalid Email")
    
# str = 'john@gmail.com'
# pattern ='@'
# for x in str:
#     if x==pattern:
#         print('Valid Email')
#         break
# else:
#     print("Invalid Email")
    
# str = 'johngmail.com'
# pattern ='@'   
# flag = str.find(pattern)
# if flag>0:
#     print("Valid Email")
# else:
#     print("Invalid Email")
        
import re
#[A-Z], [0-9], \.
# str = 'fdsfsf'
# pattern ='\s'
# email = re.search(pattern, str)
# if email:
#     print("Valid Email")
# else:
#     print("Invalid Email")

# import re  
# str = "xyz@gmail.com"
# print(re.sub("gmail", "ymail", str))


# import re
# s = 'john@@gma@il.com'
# pattern = '@'
# l = re.split(pattern, s)
# print(l)


import re
txt = "Hello World"
x = re.findall("o", txt)
print(x)
