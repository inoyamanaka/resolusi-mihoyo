total_kelompok = int(input("Masukan Total Kelompok : "))
total_anak = int(input("Masukan Total Anak : "))

def pembagian_kelompok(total_kelompok,total_anak):
    daftar_anak = []
    daftar_kelompok = []
    for i in range (0,total_anak):
        nama = input(f"Nama Anak {i+1}: ")
        daftar_anak.append(nama)
    print("========================================")
    for i in range (0, total_kelompok):
        kel = []
        for j in range (0, total_anak):
            if j % total_kelompok == i:
                kel.append(daftar_anak[j]) 

        daftar_kelompok.append(kel)
        print(f"Kelompok {i+1}: {', '.join(daftar_kelompok[i])}")

pembagian_kelompok(total_kelompok,total_anak)
