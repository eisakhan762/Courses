# Problem is ---> Write A Python Program to accept marks of six students and display them in a srrted manner

s1 = int(input("Enter 1 Student Mark : "))
s2 = int(input("Enter 2 Student Mark : "))
s3 = int(input("Enter 3 Student Mark : "))
s4 = int(input("Enter 4 Student Mark : "))
s5 = int(input("Enter 5 Student Mark : "))
s6 = int(input("Enter 6 Student Mark : "))

sMarksList = [s1, s2, s3, s4, s5, s6]
sMarksList.sort()
print(sMarksList)