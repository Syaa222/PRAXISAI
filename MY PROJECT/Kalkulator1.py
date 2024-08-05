# Selamat datang di kalkulator pintar!
print ("Selamat datang di kalkulator pintar!")

# Masukkan nilai mu 
print ("Masukkan nilai mu")

select = input("Choose the option")

num1 = input ("Insert the first number")
num2 = input ("Insert the second number")


if select == "+":
    print(int(num1) + int(num2))
    #addision

elif select == "-":
    print(int(num1) - int(num2))
    #Subtraction

elif select == "x":
    print(int(num1) * int(num2))
    #Multipication

elif select == ":":
    print(int(num1) / int(num2))
    #Division

# Ini Hasilnya
print("Ini Hasilnya")