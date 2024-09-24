# string functions / methods



# # story = "Once upon a time."


# email = "avni@gmail.sdf"

# # endswith

# print(email.endswith(".com"))

# length of the string

#indexing  012345
# name =    "hi Tom hi"

# print(len(name))


# print(name[0])

# print(name.count("T"))
#        012345
# story = "once upon a time."

# print(story.capitalize())
# print(story.upper())
# print(story.lower())

# print(story.replace("a", "sdfghj"))
# print(story.find("upon"))

# escape charcters
# \n - new line
# \t - tab space

story = "once upon \t a time. \nThanks"
print(story.find("hello"))


# print(story)

# another way of multi line strings
# story = '''once upon a time. 

# Thanks'''
# print(story)



letter = '''Dear <|NAME|>
                 You are selected!
            <|DATE|>
'''

# # USER INPUT
name = input("Enter your name: ")
date = input("Enter date: ")
if (letter.find("<|NAME|") != -1):
    letter = letter.replace("<|NAME|>", name)
# 
# letter = letter.replace("<|DATE|>", date)

# print(letter)


