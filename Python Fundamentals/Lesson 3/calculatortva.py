suma_fara_TVA = float(input("Introduceti suma in LEI: "))
TVA5 = 5
TVA20 = 20

suma_cu_TVA5 = suma_fara_TVA + 5/100 * suma_fara_TVA
suma_cu_TVA20 = suma_fara_TVA + 20/100 * suma_fara_TVA

print("5% TVA din", suma_fara_TVA, "este: ", suma_cu_TVA5)
print("20% TVA din", suma_fara_TVA, "este: ", suma_cu_TVA20)