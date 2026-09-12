Pengeluaran = [
    ("Nasi Goreng", "Makan malam", 17000),
    ("Bensin", "Transportasi", 50000)
]

while True:
    print(" Catatan Pengeluaran ")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Pengeluaran")   
    print("3. Ubah Pengeluaran")
    print("4. Hapus Pengeluaran")
    print("5. Keluar")

    pilihan_menu = input("Pilih menu (1-5): ")

    if pilihan_menu == "1":
        nama_barang = input("Apa lagi yang dibeli nih: ")
        kategori_barang = input("Mbuat apa kamu beli itu?: ")
        nominal_barang = int(input("Terus berapa harganya?: "))
        Pengeluaran.append((nama_barang, kategori_barang, nominal_barang))
        print("Nambah lagi nih pengeluaran bosku, oke deh")

    elif pilihan_menu == "2":
        print("Mau lihat daftar pengeluaran?:")
        total_pengeluaran = 0
        nomor = 1
        for i, (nama, kategori, nominal) in enumerate(Pengeluaran, start=1):
            print(f"{i}. {nama} - {kategori}: Rp {nominal}")
            total_pengeluaran = total_pengeluaran + nominal
            nomor = nomor + 1

        print(f"Total pengeluaran audah Rp {total_pengeluaran} bosku")

    elif pilihan_menu == "3" :
        nomor_barang = int(input("Masukkan nomor barang kamu yang mau diubah: "))
        index_barang = nomor_barang - 1

        if index_barang >= 0 and index_barang < len(Pengeluaran):
            nama_barang_baru = input("Masukkan nama barang yang baru:")
            kategori_barang_baru = input("Masukkan kategori barang yang baru:")
            nominal_barang_baru = int(input("Masukkan harga barang yang baru:"))

            Pengeluaran[index_barang] = (nama_barang_baru, kategori_barang_baru, nominal_barang_baru)

            print("Udah di ubah nih bos, jangan sampe salah bos.")
        else:
            print("Nomor barangnya gaada bos, anda yakin ada punya barang itu bosku?")

    elif pilihan_menu == "4":
        nomor_barang = int(input("Masukkan nomor barang yang mau dihapus.: "))
        index_barang = nomor_barang - 1

        if index_barang >= 0 and index_barang < len(Pengeluaran):
            Pengeluaran.pop(index_barang)
            print("Udah dihapus nih bos, awas aja sampe salah hapus.")
        else:
            print("Gimana mau hapus kalo nomor barangnya aja gaada, ingatin lagi berapa nomornya bos.")

    elif pilihan_menu == "5":
        print("Oke bos, semuanya sudah dicatat, jangan lupa lebih hemat lagi ya bosku")
        break
        print("Sekali lagi, lebih hemat lagi ya bosku, jangan sampe boros lagi")