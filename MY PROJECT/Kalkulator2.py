# Selamat datang di kalkukator Mine!
print("Selamat datang di kalkulator Mine")

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y # ret: mengendalikan nilai dari sebuah fungsi 

def kali(x, y):
    return x * y

def bagi(x, y): # def: Mendefinisikan fungsi
    if y != 0:  # if: mengendalikan alur program
        return x / y
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."

def main():
    print("Pilih operasi:")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. :")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ['1', '2', '3', '4']:
        angka1 = float(input("Masukkan angka pertama: ")) #mengubah nilai numerik menjadi floting 
        angka2 = float(input("Masukkan angka kedua: "))

        if pilihan == '1': 
            print(f"Hasil: {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"Hasil: {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"Hasil: {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"Hasil: {bagi(angka1, angka2)}")
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
