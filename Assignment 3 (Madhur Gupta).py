#!/usr/bin/env python
# coding: utf-8

# # Game of "Functions"

# In[ ]:


no_of_elements = int(input("Enter no. of elements:"))

list1 = []

for i in range(0,no_of_elements):
    list_element = int(input("Enter the number"))
    list1.append(list_element)

def gameOfFucntions(list2):
    _sum=0
    for i in list2:
        _sum=_sum+i
    return _sum

Sum_of_List_Elements = gameOfFucntions(list1)
print("Sum of all elements in this list", Sum_of_List_Elements)


# # String inside the function
# 
# 

# In[ ]:


String1 = input("Enter String:")

def stringReverse(String2):
    reversedString = " "
    
    for i in String2:
        reversedString = i+reversedString       
    return reversedString

_output=stringReverse(String1)
print(_output)


# # Calculate the Upper and The lower Case

# In[ ]:


inputString = input("Enter String: ")

lowerCount = 0
upperCount = 0

def caseCounter(inputString):
    
    for i in inputString:
        global lowerCount
        global upperCount
        if i.islower():
                lowerCount+=1
        elif i.isupper():
                upperCount+=1
        else:
            pass
    return upperCount,lowerCount


caseCounter(inputString)

print("Upper Case: ",upperCount)         
print("Lower Case: ",lowerCount)


# In[ ]:




