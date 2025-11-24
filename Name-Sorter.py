#Asks to see if text is separated by spaces or lines
answer = input("If the names are done using spaces between use (1) If names are done per line use (2): ")
if answer == "1":
    #If separated by spaces it writes and saves the organized list as "Organized.txt"
    with open('Project 1\\Version 2\\NameList.txt','r') as f:
        rawData = f.readline()
        splitData = rawData.split()
        splitData.sort()
        with open('Project 1\\Version 2\\Organized.txt','w') as f:
                f.writelines(splitData)
elif answer == "2":
    #If separated by lines it writes and saves the organized list as "Organized.txt"
    with open('Project 1\\Version 2\\NameList.txt','r') as f:
        rawData = f.readlines()
        oList = rawData.sort()
        with open('Project 1\\Version 2\\Organized.txt','w') as f:
                f.writelines(rawData)
else:
    quit
#quits program if any other information is given!