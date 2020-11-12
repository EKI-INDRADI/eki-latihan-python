# Belajar Membuat Method / Function


# func di eksekusi dari atas ke bawah karena masih async

nama = []

def print_nama():
    print("=================")
    for data in nama:
        print(data)

nama.append("eki1")
print_nama()

nama.append("eki2")
print_nama()

nama.append("eki3")
print_nama()