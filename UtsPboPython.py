a = True
atmumum=0
atmtabungan=0

while(a):
    print("Bank ATM PYTHON")
    print("--------------------")
    print("[1] Informasi Saldo")
    print("[2] Tambah Saldo")
    print("[3] Ambil Saldo")
    print("[4] Keluar ATM")
    print("--------------------")
    option=int(input("Pilih Menu:"))

    if option==1:
        print("Saldo atm umum Anda saat ini adalah: Rp.",atmumum)
        print("Saldo atm tabungan Anda saat ini adalah: Rp.",atmtabungan)
        print("--------------------")
    elif option==2:
        print("[1] ATM Umum")
        print("[2] ATM Tabungan")
        option2=int(input("Pilih Penyimpanan:"))
        print("--------------------")
        if option2==1:
            option3=int(input("Nominal yang akan ditambahkan :"))
            atmumum=atmumum+option3
            print("Saldo umum Anda saat ini adalah:",atmumum)

        elif option2==2:
            option4=int(input("Nominal yang akan ditambahkan :"))
            atmtabungan=atmtabungan+option4
            print("Saldo umum Anda saat ini adalah:",atmtabungan)

    elif option==3:
        print("[1] ATM Umum")
        print("[2] ATM Tabungan")
        opsiambil=int(input("Pilih saldo yang akan diambil :"))

        if opsiambil==1:
            ambiluang=int(input("Saldo yang akan diambil:"))
            atmumum=atmumum-ambil
            print("Saldo Anda saat ini adalah:",atmumum)

        elif opsiambil==2:
            ambil=int(input("Saldo yang akan diambil:"))
            atmtabungan=atmtabungan-ambiluang
            print("Saldo Anda saat ini adalah:",atmtabungan)
    elif option==4:
        exit(0)
