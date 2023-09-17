# # Convert to lowercase to Uppercase letter using for loop: -
# l=[input("Enter the list items: ")]
# print("Lower Case List: ",l)
# l1=[]
# for i in l:
#     l1.append(i.upper())
# print("Upper Case List: ", l1)

""" Q.2 :- Multiple data type in a list, so how to extract and the like number date type is going different list and
String data type is going  to string list.
"""
l1=["hello",45,2,85.50,"world",'satya']
print("Multiple Date: ", l1)
Num_list=[]
Str_list=[]
for i in l1:
    #Given the condition in if statement or Using Decision-Making Statement:
    if type(i)==int or type(i)==float:
        Num_list.append(i)
    else:
        Str_list.append(i)

print("Number List: ",Num_list)
print("String List: ", Str_list)
