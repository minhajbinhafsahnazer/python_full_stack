#coding challenge 1

#Number of Vowels and consonants in a string

string = {'A','E','I','O','U'}
vowels = 0
consonant = 0

lang=input("Enter the String : ")
for i in lang:
    if lang is in string:
        vowels+=1
    else:
        consonant+=1
print("No of vowels :", vowels)
print("No of consonants :",consonant)
