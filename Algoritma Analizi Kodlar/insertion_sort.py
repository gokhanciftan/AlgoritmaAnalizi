def insertion_sort(dizi):
  for i in range(1, len(dizi)):
        anahtar = dizi[i]
        j = i - 1
        while j >= 0 and anahtar < dizi[j]:
            dizi[j + 1] = dizi[j]
            j -= 1
        dizi[j + 1] = anahtar

# Test
dizi = [12, 5, 6, 9, 8, 14, 10, 4, 2, 1]
insertion_sort(dizi)
print("Sıralanmış Dizi:", dizi)
