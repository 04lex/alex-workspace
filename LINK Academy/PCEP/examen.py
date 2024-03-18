# def mysum(*numere):
#     suma = 0
#     for nr in numere:
#         suma += nr
#     return suma

# print(mysum(1,2,3))



# def mysum(*numere):
#     suma = 0
#     return 




## mysum((1, 2, 3)) -> (1,2,3) este un singur element, atunci punem steluta
##              mysum(*(1,2,3))
## si devine element mysum(1, 2, 3)

### Recursivitate

# def mysum(*numere) -> int:
#     return numere[0] if len(numere) == 1 else (numere[0] + mysum(*(numere[1:])))


# print(mysum(1,2,3))

from functools import reduce
def mysum(*numere) -> int:
    return reduce(lambda x, y: x + y, numere)