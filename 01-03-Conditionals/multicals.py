import os

os.system('cls')
os.system("D") #color

while True: #anu

    # 1. The app shows welcome display 
    print ("hallo kalkulator pintar!")
    print ("")

    # 2. The app asks the user's options 
    print ("""Masukkan pilihan oprasi:
        a. Pertambahan
        b. Pengurangan 
        c. Perkalian
        d. Pembagian     
    """)

    num1 = input ("Insert the first number")
    num2 = input ("Insert the second number")

    select = input("Choose the option")

    if select == "a":
        print(int(num1) + int(num2))
        #addision

    elif select == "d":
        print(int(num1) - int(num2))
        #Subtraction

    elif select == "c":
        print(int(num1) * int(num2))
        #Multipication

    elif select == "p":
        print(int(num1) / int(num2))
        #Division

    # 3.The app asks for user's, The first number
    print ("Insert the first number")

    # 4.The app asks for user's, The second number
    print ("Insert the second number")

    # 5.Gift the result for Addition
    print (input)

    # 6.The app asks the user's options
    if select == "Delete":
        print(int("choose the option30"))
    
    

  