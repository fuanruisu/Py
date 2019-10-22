#Nombre: Test_1.py
#Objetivo: First unit exam
#Autor: Juan Luis Magaña Paz
#Fecha: September 5th 2019
import os
t=("Juan", "Pedro", "Pablo","Bruno","Chencho")
#function that prints a custom message for each element in the tuple
def tupla():    
    print("-----------------------------------------------------------")
    for i in t:
        print("Dear ",i," vote for me")

    

#vowels function analize if there are vowels in the ingressed string 
# if there are, print the vowels founded, if doesn´t found anyone
#prints there's no vowel in the sentence
def vowels(cad):
    a=(cad.find('a'))
    A=(cad.find('A'))
    e=(cad.find('e'))
    E=(cad.find('E'))
    i=(cad.find('i'))
    I=(cad.find('I'))
    o=(cad.find('o'))
    O=(cad.find('O'))
    u=(cad.find('u'))
    U=(cad.find('U'))

    
    if (a>=0 or A>=0):
        print("a")
    if(e>=0 or E>=0):
        print("e")
    if(i>=0 or I>=0):
        print("i")
    if(o>=0 or O>=0):
        print("o")
    if(u>=0 or U>=0):
        print("u")
    if(a<0 and A<0 and e<0 and E<0 and I<0 and O<0 and U<0 and i<0 and o<0 and u<0):
        print("There´s no vowels in the sentence")
    cuenta = 0
    for carac in cad:
        if (carac== 'a' or carac=='A' or carac=='e' or carac=='E' or carac=='i' or carac=='I' or carac=='o' or carac=='O' or carac=='u' or carac=='U'):
            cuenta += 1
    print("The number of vowels are",cuenta)
        

def main():
    
    #Ingress a string from user
    cad=(input("Ingress a sentence\n"))
    os.system("cls")
    print("------------START---------")
    #Print the lenght of the string
    la=len(cad)
    print("The lenght of the sentence is: -->",la,"\n")
    #Call the function vowels
    print("The found vowels are: -->")
    vowels(cad)
    #Prints string in reverse
    print("The sentence in reverse is: -->")
    txt = cad[::-1]
    print(txt)
    #Ingress a blank space between each letter
    print("Blank space: -->")
    blnk_spce=" ".join(cad)
    print(blnk_spce)
    #Uppercase the first letter of each word in the string
    print("Uppercase letters: -->")
    cad2=cad.title()
    print(cad2)
    #Analyze if the string is a palindrome
    if(cad==txt):
        print("------The sentence is a palindrome------")
    else:
        print("------The sentence is no a palindrome------")
    #Call the tupla function
    tupla()
    
    
   
    

    


if __name__=="__main__":
        main()