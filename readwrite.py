# # Reading a text file
# with open('myfile.txt') as f:
#     full_text = f.read()

# print(full_text)


# # Writing a text file
# with open('testwrite.txt', 'w') as f:
#     f.write('hello')
#     f.write('\n')



# Reading name text file
with open('name.txt') as f:
    name = f.read()

# Writing hello text file
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' + name + '.\n')
    f.write('\n')

