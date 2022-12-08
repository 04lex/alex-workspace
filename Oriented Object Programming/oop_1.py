# x = 1
# print(type(x))
# print(isinstance(x,bool))
# print(isinstance(x,int))

# l = [ 42, 13 , 61 , 2 , -42 , 868 , 1, -11, -32, 300, 38384]
# print(max(l))

# l.sort(reverse=True) # reverse este parametru implicit

# print(l)

# print(l[-1])
# print(l[0])



# def calcul_pret_cu_tva(pret, TVA=19): # parametru implicit TVA=19, se adauga singur in functie unde nu are asignat altul
#     return pret + pret * TVA / 100

# print(calcul_pret_cu_tva(100, 20))
# print(calcul_pret_cu_tva(100))
# print(calcul_pret_cu_tva(100))
# print(calcul_pret_cu_tva(TVA=19, pret=100))

# print(list(range(10))) # 1 parametru implicit obligatoriu, ceilalti 2 se adauga
# print(list(range(3, 10)))
# print(list(range(5, 10, 2)))



# x = range # x-ul are aceleasi proprietati cu range
# print(list(x(3,10)))

# def check_if_x_exist(x, lst): # aceeasi chestie dar lunga
#     if x in lst:
#         return True
#     else:
#         return False

def check_if_x_exist(x, lst): # varianta frumoasa si simpla
    return x in lst


print(check_if_x_exist(1, [3, 41, 52, 53, 1, 32, 1]))
print(check_if_x_exist(11, [3, 41, 52, 53, 1, 32, 1]))
print(check_if_x_exist(lst = [3, 41, 52, 53, 1, 32, 1], x = 11))