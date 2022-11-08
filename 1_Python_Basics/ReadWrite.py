# to read a file first we need to open the file

file = open("text.txt")

# Read all the content of the file
# read n number of character by passing parameter
# 2 indicate to read the 2 bytes or first 2 characters
# print(file.read(2))

''' use any one of the method like read or readline'''
'''
# readline used to read the one line at a time
print(file.readline())
# if you give another readline it will start from the  above end of the readline
print(file.readline())
'''

'''
# print the all the line in the file using while loop
line = file.readline()
while line != '':
    print(line)
    line = file.readline()
'''

# when using readlines method it store lines as a list
# this is the difference between readline and readlines
line_list = file.readlines()
print(line_list)
for i in line_list:
    print(i.rstrip())

# whenever file is open do not forget to close the file
file.close()