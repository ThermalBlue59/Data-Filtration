# the inital goal is to read a files text filter for specific words.
with open('Project 1\\Version 1\\WordList.txt','r') as f:
    rawData = f.readline()
    all_Data = rawData.split()
#Words in the text file get digested into an array with the label "all_Data"
with open('Project 1\\Version 1.1\\KeyWords.txt','r') as g:
    coreKey = g.read()
    key_words = coreKey.split()
#Reads data from a filter file and creates an array with the labal "key_words"
for words in key_words:
     filter = [Data for Data in all_Data if Data == words]
     if [Data for Data in all_Data if Data == words]:
        print(filter)
# the function  "For words in keywords" filters words in the text file againt words within "key_words" and prints them out