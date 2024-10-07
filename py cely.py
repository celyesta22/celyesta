#no 1
nilai = int(input("Masukkan sebuah angka: "))
if nilai  % 2 :
 print("angka",nilai,"adalah ganjil.")
else :
  print ("angka",nilai,"adalah angka genap.")

  #no 2
nilai1 = int(input("Masukkan nilai ujian Anda (0-100):"))
if 100 >= nilai1 >= 90:
    print("Feedback: Sangat Baik")
elif 80<= nilai1 <= 89:
    print("Feedback: Baik")
elif 70<= nilai1 <= 79:
    print("Feedback: Cukup")
elif 60<= nilai1 <= 69:
    print("Feedback: Kurang")
else:
    print("Sangat Kurang")

    #no 3
usia = int(input("Masukkan usia Anda: "))
darah = int(input("Masukkan tekanan darah Anda: "))
if usia >= 60 and darah > 140:
      print("status kesehatan : Tinggi")
elif usia >= 60 and darah <= 140:
      print("status kesehatan : Normal")
elif usia <60 and darah > 130:
      print("status kesehatan : Tinggi")
elif usia <60 and darah <= 130:
      print("status kesehatan : Normal")