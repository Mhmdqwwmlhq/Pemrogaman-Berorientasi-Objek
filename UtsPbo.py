print("Bank ATM Python")
print("**********************")
print("[1] Informasi Saldo")
print("[2] Tambah Saldo")
print("[3] Ambil Saldo")
print("[4] Keluar")
print("**********************")

option=int(input("PIlih Menu:"))
if option==1:
    print("Saldo umum Anda saat ini adalah: Rp.0,-")
    print("Saldo tabungan Anda saat ini adalah: Rp.0,-")
    print("**************")
elif option==2:
    print("[1] Umum")
    print("[2] Tabungan")
    option2=int(input("Pilih Penyimpanan:"))
    print("**************")
if option==1:
    uang=0
    option3=int(input("Nominal uang yang akan ditambahkan :"))
    hasil1=uang+option3
    print("Saldo umum Anda saat ini adalah:",hasil1)

elif option==2:
    uang=0
    option4=int(input("Nominal uang yang akan ditambahkan :"))
    hasil2=uang+option4
    print("Saldo umum Anda saat ini adalah:",hasil2)

elif option==3:
    uang=0
    option2=int(input(" nominal ambil saldo:"))
    hasil3=uang-option2
print('saldo anda yang berkurang sebesar: ',hasil3)