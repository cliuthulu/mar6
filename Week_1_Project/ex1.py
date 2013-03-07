import os, sys
import string, shutil

#textList = []
#textList = os.listdir()
#path = /~/users/src/day3/Week_1_Project/original_file/
dirs = os.listdir('/home/user/src/day3/Week_1_Project/original_files/')
#print dirs
letterList = [] 
letter = string.lowercase[:3]
letter.split()
letterList.append(letter)
print letterList

#splitList = letterList[:1]
#print splitList
# letterList = ['./a/', './b/', './c/', './d/', './e/',
#  './f/', './g/', './h/', './i/', './j/', './k/', './l/', 
#  './m/', './n/', './o/', './p/', './q/', './r/'
#  './s/', './t/', './u/', './v/', './w/', './x/', './y/', './z/']

# for i in splitList:
#     os.mkdir('/home/user/src/day3/Week_1_Project/original_files/' + i)

for word in dirs:
    if word[:1] == 'a':
        shutil.move('/home/user/src/day3/Week_1_Project/original_files/'+ word,
            '/home/user/src/day3/Week_1_Project/original_files/a')
        #send to ./a
#     elif word[:1] == '':    
        #send to ./bcd ..
