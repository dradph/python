print ("Hasil Nilai UN Matematika \n ")
mn = int(input("Masukkan Nilai Anda : "))

if  mn <= 50 and mn >= 0:
    print ("nilai anda : ",mn ," \nMutu Nilai : D")
elif mn > 50 and mn <= 60:
    print ("nilai anda : ",mn ," \nMutu Nilai : C")
elif mn > 60 and mn <= 80:
    print ("nilai anda : ",mn ," \nMutu Nilai : B")
elif mn > 80 and mn <=100:
    print ("nilai anda : ",mn ," \nMutu Nilai : A")
else:
    print ("Nilai Yang anda masukkan Salah")      