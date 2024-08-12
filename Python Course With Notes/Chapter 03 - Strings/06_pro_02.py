''' Problem NO1 ---> Write a program to fill in a letter template given below
letter = <|Name|>
You are selected
Date: <|Date|> '''
letter = '''
Dear -> <|Name|>
You are selected!
Date: <|Date|>'''
print("Letetr")
Name = input("Enter Your Name : ")
Date = input("Enter Date : ")

letternew =  letter.replace("<|Name|>",Name)
letterCompleted =  letternew.replace("<|Date|>",Date)
print(letterCompleted)

# ****** Or ******
# letter =  letter.replace("<|Name|>",Name)
# letter =  letter.replace("<|Date|>",Date)
# print(letter)