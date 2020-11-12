# Belajar Set

# list => []
# tuple => ()
# set => {}

nama = {"Eki", "Joko", "Eki", "Joko", "Andi"}

nama.add("indradi")
nama.add("indradi")
nama.add("indradi")

for data in nama:
    print(data)

nama.remove("Eki")
nama.remove("Andi")

print(nama)

#print(nama[0]) #<< bakalan error




#perbedaan dengan list , dan tuple   
# list dan tuple bisa nembahkan data yang sama
# jika tuple hanya  menerima data yg sama ( akan tetap 1 yang di terimanya / unik ) , 
# tidak dapat mengakses data menggunakan index 1-1nya cara hanya menggunakan lopp
# hanya bs tambah dan hapus , tidak bs edit , dan datanya kadang tidak berurut