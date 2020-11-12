# Belajar Argument List


#*list_angkat  maksud dari * <<< adalah bisa  menambahkan angka lebih dari 1

# def jumlahkan( x , *list_angka):   <<<< jika ingin menambahkan parameter lain maka * hrs di tambahkan di yang paling belakang
# argument list  (*)   <<< hanya bisa 1 tidak bisa  def jumlahkan( x , *list_angka, *list_angka): 
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10, 10, 10, 10, 10, 10) #<<< contoh 