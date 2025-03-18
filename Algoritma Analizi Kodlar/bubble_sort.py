def bubble_sort(dizi):
    n = len(dizi)
    for i in range(n):
        degisti = False
        for j in range(0, n - i - 1):
            if dizi[j] > dizi[j + 1]:
                dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]
                degisti = True
        if not degisti:
            break

# Test
dizi = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(dizi)
print("Sıralanmış Dizi:", dizi)
