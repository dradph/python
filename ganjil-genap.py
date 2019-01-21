angka = int(input("Masukkan angka :"))

if angka == 0:
    print ("Bilangan 0")
elif angka < 0:
    print ("Bilangan Negatif")
elif angka % 2 == 0:
    print (angka, "adalah Genap")
else:
    print (angka, "adalah Ganjil")