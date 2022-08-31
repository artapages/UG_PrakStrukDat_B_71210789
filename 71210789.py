cekDigit = 'Ya' or 'Tidak / Q'
while cekDigit == 'Ya':
    print("Menu kalkulator yang tersedia: \n1. Penambahan \n2. Pengurangan \n3. Perkalian \n4. Pembagian \n5. Keluar (Q)")

    pilih = int(input("Masukkan pilihan anda! [cnth : 1, 2, dll] : "))
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))

    if pilih == 1:
        pilih = bil1 + bil2
        print("Hasil dari", bil1, "+", bil2, "=", pilih)
    elif pilih == 2:
        pilih = bil1 - bil2
        print("Hasil dari", bil1, "-", bil2, "=", pilih)
    elif pilih == 3:
        pilih = bil1 * bil2
        print("Hasil dari", bil1, "*", bil2, "=", pilih)
    elif pilih == 4:
        pilih = bil1 / bil2
        print("Hasil dari", bil1, "/", bil2, "=", pilih)

    cekDigit = str(input("Ingin cek lagi? Ya / Tidak(Q) : "))
    print("-----" *7) 