#FunB
#Christophoros Prodromou
#Stefanos Avraam

import funA

def functionServerless():
    #Read a string
    message = input("Enter a string: ")
    #Call the function and print result
    x=0
    while x<1000:
        counter = funA.countWords(message)
        x=x+1

    print("\nThe number of words in the string you have entered is: "+str(counter))