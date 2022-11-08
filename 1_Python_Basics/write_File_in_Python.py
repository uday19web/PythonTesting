# if we dont want to file close for the file we can use "with" method
'''
read the file and store all lines in list
reverse the list
write the list back to the file
'''

# we open the file different modes in python like read, write
# 'w' indicates to file open in write mode.
with open('text.txt', 'r') as reader:
    content = reader.readlines()

    # reverse method is to reverse the order in the list
    reversed(content)

    # write the replace the current text ahd write
    with open('text.txt', 'w') as writer:
        # using for loop to write the file
        for line in reversed(content):
            writer.write(line)