# Belajar Tipe Data Dictionary
# agar cara memanggil aranya tidak menggunakan no index
# tetapi menggunakan value stringnya.
# list = pake no index , dictionary = pake string

customer = {"Name":"Eki", "Age":26, "Address":"Subang"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Indradi"

del customer["Address"]

for key, value in customer.items():
    print(f"{key}:{value}")
# for key in customer.items():
#     value = customer[key]


    # print(f"{key[0]}:{value[0]}") #<<== example  data tupple  https://www.youtube.com/watch?v=ygy6nT_0PZ8&list=PL-CtdCApEFH_HY6bL3JER8WJOxz1nb3_H&index=35
    # print(customer.items()) #<<< merupakan dictionary == merupakan data tupple (bisa di tambah dah di hapus)

