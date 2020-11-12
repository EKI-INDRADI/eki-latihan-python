# Belajar For Loop

pelanggan = ["eki", "budi", "joko", "andi"]

pelanggan.append("Eki")
pelanggan.append("Indradi")

# Mengakses semua nama pelanggan?
#agar tidak print(pelanggan[0])  satuper satu 
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
for nama in pelanggan:
    print("------------------------")
    print(f"Nama Pelanggan : {nama} , Index ke: {pelanggan.index(nama)}")
    print("------------------------")