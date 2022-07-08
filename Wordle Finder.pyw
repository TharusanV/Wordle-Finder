listOfWords = []
alphabet = ["a", "b" , "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

inUse = True
validNumOfLettersChecker = True
validLetterGreyChecker = True
validLetterYellowChecker = True
validLetterGreenChecker = True
validRestartChecker = True

while inUse == True:
    listOfWords *= 0
    
    wordFile = open("words.txt", "r")
    for a in wordFile:
        if len(a) == 6:
          listOfWords.append(a)
        else:
            continue
    wordFile.close()
   
    while validNumOfLettersChecker == True:        
        try:
            numberOfLettersYellow = int(input("How many letters are yellow: "))
            numberOfLettersGreen = int(input("How many letters are green: "))
            numberOfLettersGrey = int(input("How many letters are grey: "))
            if numberOfLettersYellow >= 0 and numberOfLettersYellow <= 5 and numberOfLettersGreen >= 0 and numberOfLettersGreen <= 5 and numberOfLettersGrey >= 0 and numberOfLettersGrey <= 21:
                break
            else:
                continue
        except:
            print("Please input a number")


    for b in range(numberOfLettersGrey):
        while validLetterGreyChecker == True:
            try:
                invalidLetter = input("Enter the letter (Grey): ")
                break
            except:
                print("Not a letter. Try again")

        for greyWordCheck in listOfWords[:]:
            if invalidLetter in greyWordCheck:
                listOfWords.remove(greyWordCheck)


    for c in range(numberOfLettersYellow):
        while validLetterYellowChecker == True:
            try:
                storeLetterYellow = input("What's the letter (Yellow): ")
                storeIndexYellow = int(input("What's the position (0-4): "))
                if storeLetterYellow in alphabet != True and storeIndexYellow < 0 and storeIndexYellow > 4:
                    print("Not a letter or the index is not in the range. Try again")
                    continue
                else:
                    break
            except:
                print("Not a number. Try again")

        for yellowWordCheck in listOfWords[:]:
            if storeLetterYellow in yellowWordCheck[storeIndexYellow] or storeLetterYellow not in yellowWordCheck:
                listOfWords.remove(yellowWordCheck) 


    for d in range(numberOfLettersGreen):
        while validLetterGreenChecker == True:
            try:
                storeLetterGreen = input("What's the letter (Green): ")
                storeIndexGreen = int(input("What's the position (0-4): "))
                if storeLetterGreen in alphabet != True and storeIndexGreen < 0 and storeIndexGreen > 4:
                    print("Not a letter or the index is not in the range. Try again")
                    continue
                else:
                    break
            except:
                print("Not a letter. Try again")

        for greenWordCheck in listOfWords[:]:
            if storeLetterGreen not in greenWordCheck[storeIndexGreen] or storeLetterGreen not in greenWordCheck:
                listOfWords.remove(greenWordCheck) 


    print("All possible words: ")
    for allPossibleWords in listOfWords:
        print(allPossibleWords)

    while validRestartChecker == True:
        try:
            restart = input("Would you like to restart (Y/N): ")
            if restart == "y" or restart == "Y":
                print("Make this day a good one brother")
                break
            if restart == "n" or restart == "n":      
                inUse = False
            else:
                print("Please enter Y or N")
                continue
        except:
            print("Invalid input. Please try again")
            
                
        
            
                
                

                

