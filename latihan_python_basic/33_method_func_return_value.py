# Belajar Method Return Value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka   #<<< total ini tidak bs di panggil di luar
        # return total        #<<< agar bs di panggil di luar  dibuatlah return
    return (list_angka, total)  #menggunakan tupple (tidak bs berubah , supaya bs return list_angka dan tidak berubah2 angkanya )

list_angka, total = jumlahkan(10, 10, 10, 10, 10)  #<<< 
 
# Mengambil data total?
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
