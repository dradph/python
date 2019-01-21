print ("PENGHITUNG NILAI \n ")
n = int(input("Masukkan Nilai Anda : "))

if  n < 70 and n >= 0:
    print ("nilai anda : ",n ," \nMutu Nilai : D")
elif n >= 70 and n < 75:
    print ("nilai anda : ",n ," \nMutu Nilai : C")
elif n >= 75 and n < 80:
    print ("nilai anda : ",n ," \nMutu Nilai : B")
elif n >= 80 and n <=100:
    print ("nilai anda : ",n ," \nMutu Nilai : A")
else:
    print ("Nilai Yang anda masukkan Salah")      