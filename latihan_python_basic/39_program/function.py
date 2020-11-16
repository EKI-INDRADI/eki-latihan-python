# Program Management Kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("======================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("No telepon yang akan dihapus : ")

    index = -1 # variable tampung -1 untuk data tidak ketemu

    for i in range(0, len(daftar_kontak)): #pencarian no index untuk hapus
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]: #kalo udah ketemu dpt indexya
            index = i #di set indexnya
            break

    if index == -1: # maksud -1 adalah jika index tidak ketemu
        print("Data kontak tidak ditemukan")
    else:
        del daftar_kontak[index] #stlh index ketemu baru di delete berdasarkan index arr
        print("Berhasil menghapus data kontak")

def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("======================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
