nama_barang = input("Nama Barang     : ")
harga_satuan = float(input("Harga Barang    : "))
jumlah_barang = int(input("Jumlah Barang   : "))

subtotal_belanja = harga_satuan * jumlah_barang
ppn = subtotal_belanja * 0.11
total_bayar = subtotal_belanja + ppn

print(f"Output  : Subtotal {subtotal_belanja}, PPN {ppn}, Total Bayar {total_bayar}")