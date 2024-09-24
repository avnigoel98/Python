# print("hello world")

# # modes - r(read) , w(write), a(update)

# f = open('hello.txt', 'r')

# data = f.readline()

# print(data)



# f = open('bye.txt', 'w')

# f.write("hello i am a data from python file")

# Django / flask frameworks 


# Write a pragram to generate multiplication tables from 2 to 20 and write it to the different files.
# place them in a folder for a 13-years old.


# 2 x 1 = 2
# 2 x 2 = 4
# .....


# 2 x 10 = 20

# (start ,  end - 1)
# for i in range(2, 21):
#     f = open(f'tables/multiplication_table_of_{i}.txt', 'w')
#     for j in range(1, 11):
#         f.write(f"{i} x {j} = {i*j}\n")




# name = "Tom"
# print("hello " + name )
# # f-strings 
# print (f"hello {name}")


# A file contains a word "Donkey" multiple times.
# we need to replace this word with ###$$$ 



f = open("random.txt" , "r")
data = f.read()

data = data.replace("donkey" , "######")

f = open("random.txt", "w")
f.write(data)