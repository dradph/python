print ("PENGHITUNG NILAI #2 \n ")
n = int(input("Masukkan Nilai Anda : "))

if  n <= 45 and n >= 0:
    print ("nilai anda : ",n ," \nMutu Nilai : D")
elif n <= 50 and n > 45:
    print ("nilai anda : ",n ," \nMutu Nilai : D+")
elif n <= 55 and n > 50:
    print ("nilai anda : ",n ," \nMutu Nilai : C-")
elif n <= 60 and n > 55:
    print ("nilai anda : ",n ," \nMutu Nilai : C")
elif n <=  65 and n > 60:
    print ("nilai anda : ",n ," \nMutu Nilai : C+")
elif n <=  70 and n > 65:
    print ("nilai anda : ",n ," \nMutu Nilai : B-")
elif n <=  75 and n > 70:
    print ("nilai anda : ",n ," \nMutu Nilai : B")
elif n <=  80 and n > 75:
    print ("nilai anda : ",n ," \nMutu Nilai : B+")
elif n <=  85 and n > 80:
    print ("nilai anda : ",n ," \nMutu Nilai : A-")
elif n <=  100 and n > 85:
    print ("nilai anda : ",n ," \nMutu Nilai : A") 
else:
    print ("Nilai Yang anda masukkan Salah")             
    