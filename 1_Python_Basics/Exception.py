
itemsincart = 0
# 2 items will be added to cart

if itemsincart != 2:
    # raise Exception("Products Cart Count not matching")
    pass

# one more way to raise the error is "assert"
assert (itemsincart == 0) # if the condition is True it will throw the error.

# Try , except mechanism
# if you think the code throw error put it in try block
# it will not stop the code

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("Try block has error")

# if you want to know the what python show as error
# we have to use "exception" in except block
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e: # storing exception in 'e' variable
    print(e)

# "finally" keyword execute as well if the try or except block executed
finally:
    print("Cleaing up resources")

