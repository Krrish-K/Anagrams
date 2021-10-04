# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:49:52 2020

@author: krish
"""
str1=input("Enter 1st String:")
str2=input("Enter 2nd String:")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("These are Anagrams")
else:
    print("These are not Anagrams")