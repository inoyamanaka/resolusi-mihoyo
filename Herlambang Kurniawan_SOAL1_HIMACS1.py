nilai_wawan = [70,30,50,90,80]
nilai_dadang = [50,50,70,80,80]

def perbandingan(a,b):
    skor = []
    for i in range (0,len(nilai_wawan)):
        skor.append("w" if nilai_wawan[i] >= nilai_dadang[i] else "d")
    res = {i:skor.count(i) for i in skor}
    return (f"{res['w'],res['d']} || Wawan = {res['w']}, Dadang = {res['d']}")

print(perbandingan(nilai_wawan, nilai_dadang))