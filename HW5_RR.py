"""
Ronald Ramirez
CS100 2024S Section 006
HW 05 February 14 2024
"""

#1
months = ["January","February", "March", "April", "May", "June", "July", "August","November","December"]
#prints out the all the months that start with letter J
for i in months:
    if "J" in i:
        print(i)
        
print("-------")
#2

for j in range(0,100):
    if j % 2 == 0 and j%5 == 0:
        print(j)
        
print("-------")
#3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for letter in horton:
    if letter in vowels:
        print(letter)
        

