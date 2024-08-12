# greeting = "Good morning, "
# name = "Eisa Khan"
# # print(type(name))
# print(greeting + name) # when we use '+' in string it concatenates the string

name = "Eisa Khan"
# ********* String slicing *********
print("The Char in 0 index of name is",name[0]) # Enter Index number in ['here'] to get the desired char, remember in python index starts from 0
# name[3] = 'm'  does not work

print("The char bttween 0 index to 4 length is",name[0:4]) # printing in terminal form 0 index to 4 index

print("The char bttween :4 index is",name[:4]) # when we dont enter anything in start index the the slicing starts from 0 index to end index entered by programmer

print("The char bttween 1: index is",name[1:]) # when we dont enter anything in wnd index the the slicing starts from programmer index to end index of string

# ********* String slicing with negative index *********
# we use negative index to slice string from end, negative index starts form '-1'
print("The lat Char of 'name' var is",name[-1]) # we use -1 to get last char of string

print("The Value between -4 to -1 length is", name[-4:-1])


# ********* String slicing with skiping vakue *********
print(name[0::3]) # printing value between 0 index to strings lenght and skipping every 3-1 chars


# ********* getting string length using len() function *********
print("The Length of name is",len(name))