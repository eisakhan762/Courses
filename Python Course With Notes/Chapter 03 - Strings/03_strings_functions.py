story = "once upon a time there was a youtube named harry who uploaded python course with notes"
print(story[0:5])

# ********* String functions *********
print("The Length of story is :",len(story))

print("Is story ends with khan :",story.endswith("khan"))

print("Is story starts with Once :",story.startswith("Once"))

print("check how many 'e' in story string :",story.count("e"))

print('''using to capitalize first char of story :''',story.capitalize(),'''
''')
print('''finding is harry available in story string
if available in string it shows the start index of harry
if not availabel in string it shows in the terminal '-1' :''',story.find("harry"))

print("replacing harry with eisa khan :",story.replace("harry","eisa khan")) # if we enter a string which is not available in string it does not show error but also don't replace, it will also replace all the world in the string 'harry' to 'eisa khan'
