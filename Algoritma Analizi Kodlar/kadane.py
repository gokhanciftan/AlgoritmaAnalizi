def kadane(dizi):
    maks_toplam = float('-inf')
    gecici_toplam = 0

    for sayi in dizi:
        gecici_toplam = max(sayi, gecici_toplam + sayi)
        maks_toplam = max(maks_toplam, gecici_toplam)
    
    return maks_toplam

# Test
dizi = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maksimum Alt Dizi Toplam:", kadane(dizi))
