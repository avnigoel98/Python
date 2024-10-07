# conditional statements

# a = 45
# if(a > 3):
#     print("The value of a is greater than 3")
# elif(a > 7):
#     print("The value of a is greater than 7")
# elif(a > 12):
#     print("The value of a is greater than 12")
# elif(a > 15):
#     print("The value of a is greater than 15")
# else:
#     print("The value is not greater than 3 or 7 or 12 or 15")

# if(a > 8):
#     print("hello")

# if(a > 900):
#     print("hi")


# age = int(input("Enter your age: "))

# # voting system
# if(age > 18):
#     print("You can vote")
# else:
#     print("cant vote")

# # "27" -> string
# # 27 -> int

# if("12" == 12):
#     print("equal")
# else:
#     print("not equal")

# and -> both statements should be true
# or -> one of them should be true 
# age = int(input("Enter your age: "))
# if(age > 34 or age < 56):
#     print("you can work with us")
# else:
#     print("you cannot work")
# print("bye")


# is (keyword)

# a = None
# if (a is None):
#     print("yes")
# else:
#     print("No")

# in (keyword)

# a = [12, 67, 89, 13]
# print(670 in a)

# A spam comment is defined as the following keywords:
# "buy now" , "subscribe this", "make a lot of money", "click this"

# we need to detect these spam comments

# text = input("Enter the text: ")

# if("buy now" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam = False

# if(spam == True):
#     print("spam")
# else:
#     print("Not spam")


# names = ["Harry", "Tom", "Rohan"]

# user = input("Enter user's name to check: ")
# user = user.capitalize()
# if (user in names):
#     print("yes present")
# else:
#     print("not prsent")

# for, while


# for i in range(10):
#     if(i == 5):
#         break # come out of the loop, as loop has ended
#     print(i)

# for i in range(10):
#     if(i == 5):
#         continue # skip and go on in the loop
#     print(i)

# for i in range(10):
#    pass 

# for i in range(100):
#     pass

# if(12 > 100):
#     pass

# print("hello")

names = ["Harry", "Tom", "Rohan", "Rahul"]

for i in names:
    if i.startswith("R"):
        print("Hello " + i)    