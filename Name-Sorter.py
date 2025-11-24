# the inital goal is to read a files text filter for specific words.
with open('Project 1\\Version 1\\WordList.txt','r') as f:
    rawData = f.readline()
    all_Data = rawData.split()
#Words in the text file get digested into an array with the label "all_Data"
key_words = ["dog","and","the"]
#the variable "key_words" creates a catalog of words to search against
for words in key_words:
     filter = [Data for Data in all_Data if Data == words]
     if [Data for Data in all_Data if Data == words]:
        print(filter)
# the function  "For words in keywords" filters words in the text file againt words within "key_words" and prints them out