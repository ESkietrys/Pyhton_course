
# Kintamasis, pvz.: Vardas = "Modestas"; skaicius = 25

# vardas = "Eugenijus"
# skaicius = 25
#
# print("mano sugalvotas skaicius " + str(skaicius))
#
# active_user = True
# fruits = ['apple', 'orange', 'kiwi', 'arbuziks']
# print(fruits)
# viskas prasideda nuo 0
# print(type(true_or_false))

# Lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Antantas',
#     'Amzius': 34,
#     'Miestas': 'Klaipeda'
# }
# print(lietuvos_pilietis)
# print("Pries:")
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# print("Po: ")
# Lietuvos_pilietis['Vardas'] = "Giedrius"
# print("Vardas: ", lietuvos_pilietis["Vardas"])
# # print(type(fruits))

# Temperatūros = [20, 25, 22, 18, 12]
#
# suma = sum(Temperatūros)
# print(suma)
#
# kiekis = len(Temperatūros)
# print(kiekis)
#
# vidutine_temp = suma / kiekis
# print("vidutinė temperatūra yra: ", vidutine_temp)
#
# sudėtis = 5
# laipsnis = 2 ** 3
# liekana po dalybos = 10 % 3
# dalyba_be_liekanos (TIK sveikas skaicius) = 15 // 3

# If'as'

import random
import string


# IFAS
# skaicius = 42
#
# if skaicius == 42:
#     print("lygus")
# else:
#     print("Nelygus")

# skaicius = 42
#
# if skaicius < 42:
#     print("daugiau uz 42")
# elif skaicius == 42;
#     print("Lygu")
# else:
#     print("Nelygus")

# FORAS

# sarasas = [1,2,3,4,5]
# for elementas in sarasas:
#     print("Elementas: ", elementas)


# for i in range(5):
#     print(i)

# for i in range(2, 7):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)
# reversas

# skaiciai = [24, 11, 72, 34, 7, 84]
#
# didziausias_skaicius = skaiciai[0]
#
# for skaicius in skaiciai:
#     if skaicius > didziausias_skaicius:
#         didziausias_skaicius = skaicius
# print("Didziausias skaicius: ", didziausias_skaicius)

# skaicius = input("Koks tavo vardas?: ")
# print(skaicius)

# skaicius = int(input("Parasykite skaiciu: "))
# print(skaicius)

# skaicius = float(input("Parasykite skaiciu: "))
# print(skaicius)

# skaicius = int(input("Parasykite skaiciu: "))
# suma = 0
#
# for i in range(1, skaicius + 1):
#     suma += i
# print("skaiciu suma nuo i iki ", skaicius, "yra", suma)

# užduotis: reikia iš sčrašo išfiltruoti lyginius skaičius

# sarasas = [2,5,11,22,9]
# # reikia papildomo listo
# lyginiai_skaiciai = []
#
# for skaicius in sarasas:
#     if skaicius % 2 == 0:
#         lyginiai_skaiciai.append(skaicius)
# # append prideda i nauja sarasa
# print("lyginiai skaiciai: ", lyginiai_skaiciai)

# eiluciu_sk = int(input("Įveskite sveiką skaičių "))
# for eilute in range(1, eiluciu_sk+1):
#     tarpas = eiluciu_sk - eilute
#     zvaigzd = 2 * eilute -1
#     print(" " * tarpas + "*" * zvaigzd)
# tarpo printas " " (su space)

# surasti pirminius skaičius iš intervalo tarp 10 ir 50

# pradzia = 10
# pabaiga = 50
# print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# for skaicius in range(pradzia, pabaiga + 1):
#     if skaicius > 1:
#         for daliklis in range(2, skaicius):
#             if (skaicius % daliklis) == 0:
#                 break
#         else:
#             print(skaicius)

# patikrinti zodzius is saraso, atspausdinti tuos, kurie prasideda raide "A"

# zodziai = ["as", "tu", "jis", "asta", "marius"]
# raide = "a"
# for zodis in zodziai:
#     if zodis[0].lower()== raide.lower():
#         print(zodis)

# sudaryti ir isvesti daugybos lenetele

# print("Daugybos lentelė nuo 1 iki 10")
# for i in range(1,11):
#     for j in range(1,11):
#         rezultatas = i*j
#         print(f"{i} * {j} = {rezultatas}")
#     print()

# Patikrinti ar skaicius, kuri 5vede vartotojas, teigiamas, neigiamas ar nulis

# skaicius = int(input("Įveskite skaičių "))
# if skaicius > 0:
#     print("teigiamas ")
# elif skaicius < 0:
#     print("neigiamas")
# else:
#     print("nulis")

# isvesti "fizz", kurie /3, "buzz", kurie dalinasi is 5, "fizzbuzz" ir is 3 ir is 5, intervale nuo 1 iki 100

# for skaicius in range(1,101):
#     if skaicius % 3 ==0 and skaicius % 5 ==0:
#         print("fizzbuzz")
#     elif skaicius % 3 == 0:
#         print("fizz")
#     elif skaicius % 5 == 0:
#         print("buzz")
#     else:
#         print(skaicius)

# sukurkite skaičių atspėjimo žaidimą. programa sugeneruoja skaičių, o vartotojas turi atspėti per X bandymų skaičiu

# pasleptas_sk = random.randint(1,100)
# bandymai = 0
# maksimalus_bandymu_sk = 10
# while bandymai < maksimalus_bandymu_sk:
#     spejimas = int(input("atsp4kite skaiciu nuo 1 iki 100: "))
#     bandymai += 1
#     if spejimas == pasleptas_sk:
#         print(f"Sveikiname! Atspejote skaiciu per {bandymai} bandymus ")
#         break
#     elif spejimas < pasleptas_sk:
#         print("bandykite didesnį skaičių ")
#     else: print("bandykite mažesnį skaičių ")
# if bandymai >= maksimalus_bandymu_sk:
#     print(f"J8s pasiek4t max bandym7 skaiciu. pasl4ptas skaicius buvo {pasleptas_sk}")

# sukurti sarašą žodžių, kur saugomi žodžiai ir jų ilgiai, išvesti žodžius su ilgesniais nei 6 simboliai?

# zodziu_sarasas = ["kaimas", "miestas", "savivaldybė", "miestelis", "gyvenvietė", "mama", "tėtis"]
# zodynas = {}
# for zodis in zodziu_sarasas:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} raidės")


# Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus.

# trumpas_tekstas = "visi visi visi norėjo alaus, bet buvo tik tuščios alaus bačkos ir rarūgusio vyno alaus buteliuose"
# žodynas = {}
# zodziai = trumpas_tekstas.split()
# for zodis in zodziai:
#     zodis = zodis.strip(",.")
#     žodynas[zodis] = žodynas.get(zodis, 0) + 1
# for zodis, pasikartojimai in žodynas.items():
#     if pasikartojimai >=3:
#         print(f"pasikartojantis(-ys) Žodis(-iai) yra: {zodis}, pasikartojo {pasikartojimai} kartų")
#
# pasižiūrėti strip

# ilgis = 7
# simboliai = string.ascii_letters + string.digits + string.punctuation
# random_string = ''.join(random.choice(simboliai) for _ in range(ilgis))
# print("random_string", random_string)

# 2023 09 07

# vardai = ["jonas", "petras", "marius", "laura"]

# pirmas_vardas =  vardai.pop()
# print(pirmas_vardas)

# vardai.insert(1, "Giedrius")
# print(vardai) #meta į nurodytą vietą

# vardai.append("Giedrius2")
# print(vardai) #meta į galą

# vardai.sort()
# print(vardai) #asc atmaina (r86iuos nuo galo)
#
# vardai.sort(reverse=True)
# print(vardai) #desc atmaina (r86iuos nuo galo)

# vardai.remove("Giedrius")
# print(vardai) #išmeta Giedrių

# vaisiai = ("obuolys", "kriause", "banana", "braske")
#
# # vaisiai1 = ["obuolys", "kriause", "banana", "braske"]
#
# vaisiai = {
#     "obuolys",
#     "kriause",
#     "banana",
#     "braske"
#     }

# vaisiai2 = vaisiai[2]
# print(vaisiai2)

# skaiciai = (3.14, 2.71)
# x, y = skaiciai
# print(x)
# print(y)

# vaisiai1 = ["obuolys", "kriause", "banana", "braske"]
# for indeksas, vaisius in enumerate(vaisiai1, start=1):
#     print(f"{indeksas}, {vaisius}")

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame naują failą")
#     print(content)

    # w = write
    # r = read
#     a = append (pridedam)

# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
# #     content = file.read()
# #     print(content)

#
# with open("failo_pav.txt", 'a', encoding='utf-8') as file:
#     content = file.write("papildomas tekstas")
#     print(content)
#
# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     for eilute in file:
#         print(eilute.strip())

# with open("vaisiai.txt", 'r', encoding='utf-8') as file:
#     file.write('Obuolys, \nKriause, \nBananas, \nBraske') #5ra6o
#     vaisiai = file.readlines() #nuskaito
#     print(vaisiai)

