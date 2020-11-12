angka = []

# Belajar Input Number

print("Angka a : ")
a = int(input())

angka.append(a)
print("Angka b : ")
b = int(input())
angka.append(b)

print("Angka c : ")
c = int(input())
angka.append(c)



nilai = ( int(angka[0]) + int(angka[1]) ) *  int(angka[2])

print("arr list = ")
print(angka)

print("jumlah arr = ")
print(len(angka))

print(f"( {str(angka[0])} + {str(angka[1])} ) * {str(angka[2])}  =  {str(nilai)}")
