# def pasisveikinimas(vardas):
#     sveikinimas = f"Sveiki, {vardas}"
#     return sveikinimas
#
# vardas = input("Iveskite savo varda: ")
# sveikinimas = pasisveikinimas(vardas)
# print(sveikinimas)

# def ar_lyginis(skaicius):
#     if skaicius %2 ==0:
#         return True
#     else:
#         return False
#
# skaicius = 7
# if ar_lyginis(skaicius):
#     print(f"{skaicius} yra lyginis")
# else:
#     print(f"{skaicius} yra nelyginis")

# def suma(a,b):
#     rezultatas = a+b
#     return rezultatas
# x=5
# y=3
# sumos_rezultatas = suma(x,y)
# print(f"{x}+{y} = {sumos_rezultatas}")
#
# print(suma(2,3))

7# funkcijos be argumentų
#
# def suma():
#     rezultatas = a+b
#     return rezultatas
# x=5
# y=3
# sumos_rezultatas = suma()
# print(f"{x}+{y} = {sumos_rezultatas}")

# def main():
#     sveikinimas = f"Sveiki, Augi"
#     return sveikinimas
#
# if __name__ == "__main_":
#     main()

# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# sarasas = [10, 15, 20, 25, 30, 1]
# rezultatas = vidurkis(sarasas)
# print(f"sara6o vidurkis: {rezultatas}")

# ar skai2ius teigiams ar neigiams

# def teigiamas(skaicius):
#     # int(input("invesk skaiciu "))
#     if skaicius > 0:
#         return True
#     else:
#         return False
#
#
# skaicius = 4
# if teigiamas(skaicius):
#     print(f"{skaicius} yra teigiamas")
# else:
#     print(f"{skaicius} yra neigiamas")

# suras max sarase

# def maksas(skaicius):
#     didis = skaicius[0]
#     for i in skaicius:
#         if i > didis:
#             didis = i
#     return didis
#
# sarasas = [10, 658, 12, -2]
# Maksis = maksas(sarasas)
# print(f"did=iausias skaicius yra {Maksis}")

# def jungiklis(list1, list2):
#     jungtukas = list1 + list2
#     return jungtukas
#
# list1 = [20, 22]
# list2 = [1, 5]
# rezas = jungiklis(list1, list2)
# print(rezas)

# kuri suras didesni skaiciu nei nurodytas sarase

# def didesnis(listas, skaicius):
#     didis = [sk_1 for sk_1 in listas if sk_1 > skaicius] #GERA MINTIS
#     return didis
#
# listas = [1, 2, 15, 101, 1005]
# n = 8
# didesni_sk = didesnis(listas, n)
# print(f"sarase skaiciai didesni uz {n}: yra {didesni_sk}")

# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;

# def SPV(pazymiai): #SPV - studento pažymių vidurkis
#     suma = sum(pazymiai)
#     vidurkis = suma /len(pazymiai)
#     return (vidurkis)
#
# Petraitis = [0, 2, 2, 2] ##ok, bet jei laukelis tuščias, pvz. studentas dar neatsiskaitė už konkretų modulį?
# St_vid = SPV(Petraitis)
# print(f"Studento vidurkis yra {St_vid}")


# 2. Sukurkite funkciją pirminiai_skaiciai(n), kuri priima sveikąjį skaičių n,
# ir grąžina visus pirminius skaičius nuo 2 iki n;

# def pirminiai_skaiciai(n): ## neina įdėt break????
#     PS = [sk for sk in range(2, n+1) if sk > 1 for daliklis in range(2, sk) if (sk % daliklis) != 0]
#     return PS
#
# a = 7
# rezas = pirminiai_skaiciai(a)
# print(rezas)


# def pirminiai_skaiciai(n):
#     PS = []
#     for sk in range(2, n + 1):
#         pirminis = True
#         for daliklis in range(2, sk):
#             if sk % daliklis == 0:
#                 pirminis = False
#                 break
#         if pirminis:
#             PS.append(sk)
#     return PS
#
# a = 11
# rezas = pirminiai_skaiciai(a)
# print(f"pirminiai skaičiai intervale nuo 2 iki {a} yra {rezas}")

# 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;

# def didziausias_elementas(sarasas):
#     didziausias_sk = sarasas[0]
#     for skaicius in sarasas:
#         if skaicius > didziausias_sk:
#             didziausias_sk = skaicius
#     return didziausias_sk
#
# sk_sarasas = [20, 5, 1, 0, 18]
# maxas = didziausias_elementas(sk_sarasas)
# print(maxas)

# # 5. Sukurkite funkciją kvadrato_plotas(ilgis), kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.
#
# def kvadrato_plotas(ilgis):
#     KP = ilgis * ilgis
#     return KP
#
# KP = kvadrato_plotas(3)
# print(KP)

# 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą.
# Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;

# def sarasas_suma(sarasas):
#     suma = 0
#     for sk in sarasas:
#         suma += sk
#     return (suma)
#
# sarasas = []
# while True:
#     sk = int(input("įveskite sveikus skaicius (arba 0 jei norite baigti "))
#     if sk ==0:
#         break
#     else:
#         sarasas.append(sk)
#
# sumele = sarasas_suma(sarasas)
# print(sumele)

# def sarasas_suma(sarasas):
#     sarasas = []
#     while True:
#         sk = int(input("įveskite sveikus skaicius (arba 0 jei norite baigti "))
#         if sk == 0:
#             break
#         else:
#             sarasas.append(sk)
#     suma = 0
#     for sk in sarasas:
#         suma += sk
#     return (suma)
#
#
# sarasas = []
# sumele = sarasas_suma(sarasas)
# print(sumele)

# 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.

# def mano_sarasas(sarasas):
#    sandauga = 1
#    for skaicius in sarasas:
#         sandauga *= skaicius
#    return sandauga
# sk_sarasas = [2, 4, 6, 8, 10]
# print('Saraso skaiciu sandauga lygi:',mano_sarasas (sk_sarasas))