def max_crossing_sum(dizi, sol, orta, sag):
    sol_toplam = float('-inf')
    toplam = 0

    for i in range(orta, sol - 1, -1):
        toplam += dizi[i]
        sol_toplam = max(sol_toplam, toplam)

    sag_toplam = float('-inf')
    toplam = 0

    for i in range(orta + 1, sag + 1):
        toplam += dizi[i]
        sag_toplam = max(sag_toplam, toplam)

    return sol_toplam + sag_toplam

def divide_and_conquer(dizi, sol, sag):
    if sol == sag:
        return dizi[sol]

    orta = (sol + sag) // 2

    sol_maks = divide_and_conquer(dizi, sol, orta)
    sag_maks = divide_and_conquer(dizi, orta + 1, sag)
    ortadan_maks = max_crossing_sum(dizi, sol, orta, sag)

    return max(sol_maks, sag_maks, ortadan_maks)

# Test
dizi = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maksimum Alt Dizi Toplam:", divide_and_conquer(dizi, 0, len(dizi) - 1))
