"""
'r' : only read
'w' : only write -> delete all, and create a new file
'r+' : read and write
'a' : append mode --> create a new file
"""

with open('test.txt', mode='a') as my_file:
    text = my_file.write('Hey it\'s me!')
    print(text)

with open('sad.txt', mode='a') as my_file:
    text = my_file.write(':(')
    print(text)

with open('run.py', mode='a') as my_file:
    pass

with open('db/database.txt', mode='w') as my_database:
    pass
