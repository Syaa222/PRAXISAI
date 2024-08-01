def hitung_huruf(teks):
    # Membuat dictionary untuk menyimpan frekuensi huruf
    frekuensi_huruf = {}
    
    # Menghitung setiap huruf dalam teks
    for huruf in teks:
        if huruf.isalpha():  # Memastikan hanya menghitung huruf alfabet
            huruf = huruf.lower()  # Mengubah huruf menjadi huruf kecil
            if huruf in frekuensi_huruf:
                frekuensi_huruf[huruf] += 1
            else:
                frekuensi_huruf[huruf] = 1
    
    return frekuensi_huruf


# Contoh penggunaan
teks = "budi mulkidi"
hasil = hitung_huruf(teks)
print(hasil)