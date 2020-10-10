Nilai0 = 0
Nilai1 = 1

Nilai = 0
Tampung = []
Tampung.append(Nilai0)
Tampung.append(Nilai1)
while Nilai1 <4000000:
    Nilai = Nilai0 + Nilai1
    Nilai0 = Nilai1
    Nilai1 = Nilai
    if Nilai<4000000:
        Tampung.append(Nilai)
    else:
        pass

Hasil = sum(Tampung)

print(Hasil)
