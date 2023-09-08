# 2 Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą

# # Pradedame nuo to, ko neturim. Kuriam žodžių sąrašą (stengiamės (dėl patogumo) nenaudot LT raidyno)
# zodziu_sarasas = ["kas", "manes", "nenuzudo", "padaro", "stipresniu", "kas", "manes", "nelies", "nebus", "paliestas"]
#
# # Sukuriam tuščią žodyną. Jame saugosime žodžius.
# zodynas = {}
#
# # Tuomet reik paimt pirmąjį žodį (sukurpiam naują darinį 'zodis', kuris "pasiima" pirmą žodį (mano atveju "kas")
# # iš sudaryto sąrašo ir tikrina ar jis kartojasi...
# # Sąlyga if (jei/jeigu) nurodant pasikalrtojimai tikrina ar yra toks žodis tarp likusių...
# # jei taip, prideda +1, jei ne (else), palieka tą pačią reikšmę
#
# for zodis in zodziu_sarasas:
#     if zodis in zodynas:
#         zodynas[zodis] += 1
#     else:
#         zodynas[zodis] = 1
# #
# # # Išvesti unikalius žodžius ir jų pasikartojimo dažnumą
# # print("Unikalūs žodžiai ir jų pasikartojimo dažnumas:")
# for zodis, dažnis in zodynas.items():
#     print(f"Žodis  '{zodis}' yra unikalus. Jis pasikartojo {dažnis} kartą(us)")

 # 3. Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;

# students = {
#     "Jonas": 9.5,
#     "Petras": 7.8,
#     "Marius": 8.2,
#     "Elena": 9.0,
#     "Laura": 7.5
# }
# print("Studentai su mokymosi vidurkiu >= 8:")
# for vardas, vidurkis in students.items():
#     if vidurkis >= 8:
#         print(f"{vardas}: {vidurkis}")
#     else:
#         print("Gerai besimokančių studentų nėra")

# 4. Sukurti žodyną su knygų informacija ir surikiuoti knygas pagal metus ir pavadinimus.
# Knygos = {
#     "Mes vardieniai studentai": 2023,
# }
# pabaigti

# Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą,
# kur n yra vartotojo įvestas skaičius. Panaudokite "for" ciklą ir "if" sąlygos sakinį,
# kad tikrintumėte, ar įvestas skaičius yra sveikasis;

# n_tasis_sk = int(input("Įveskite skaičių "))
# if n_tasis_sk <= 0:
#     print("Įveskite teigiamą skaičių")
# else:
#     suma = 0
#     pradzia = 1
#
# for i in range(pradzia, n_tasis_sk + 1):
#     suma += i
# print(f"skaiciu suma nuo", 1 , "iki", n_tasis_sk, "yra", suma)

# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10).
# Programa turi grąžinti mokinio vertinimą (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai").
# Naudokite "if" sąlygos sakinį;

# pazymys = int(input("Įveskite pazymį "))
# if pazymys <= 2:
#     print("neužtektinai")
# elif pazymys <= 5:
#     print("silpnai")
# elif pazymys <= 7:
#     print("vidutiniskai")
# elif pazymys <=9:
#     print("gerai")
# elif: pazymys =10:
#     print("puikiai")
# else:
# pasikoreguoti jei <1 ar >10

# Alternatyva

# if pazymys < 1 or pazymys > 10:
#     vertinimas = "Netinkamas pazymyus, iveskite pazymi nuo 1 iki 10"
# elif pazymys >= 9:
#     vertinimas = "Puikiai"
# pasipildyti kitom reikšmėm
# else:
#     vertinimas = "Neuztektinai"
#
# print(f"Mokinio vertinimas: {vertinimas}")

# # # Vartotojas įveda pažymį
# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
#
# # Tikriname pažymio vertinimą
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."
#     print(f"mokinio vertinimas {vertinimas}")
# kažkas čia dar pypt ne taip, pasižiūrėsiu vėliau


# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus.
# Programa turi patikrinti, ar įvesti metai yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą;

# Metai = int(input("Įveskite metus "))
# if Metai % 4 == 0:
#     print("Jūsų įvesti metai yra keliamieji")
# else:
#     print("Deja, olimpiados šiemet nebus, nes pateikti metai nėra keliamieji")

# 4. Turite žodyną, kuriame yra vardai ir amžius.
# Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras,
# kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;

# Pradinis_zodynas = {
#     'Jonas': 18,
#     'Petras': 19,
#     'Onutė': 16,
#     'Zitute': 20
# }
# Zodynas2 = {}
# for vardas, amzius in Pradinis_zodynas.items():
#     if amzius >=18:
#         Zodynas2[vardas] = amzius
# print(f"18 ir vyresni {Zodynas2}")


# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas.
# Sukurkite sąrašą, kuriame prekės yra žodynai, kuriuose yra prekės pavadinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą.

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
# # Enteris u=baigia pirkim1
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")

# viens ifs ir du forai

# 6. Turite sąrašą žmonių vardų. Sukurkite programą, kuri leidžia vartotojui įvesti vardą ir patikrina,
# ar jis yra sąraše. Jei vardas yra sąraše, programa turi išvesti pranešimą "Vardas yra sąraše,"
# kitu atveju - "Vardo nėra sąraše."

# 2. Turite žodyną su studentų vardais ir jų pažymiais. Parašykite "for" ciklą,
# kuris išveda kiekvieno studento vardą ir jo pažymį.

# studziai = {
#     "Jonas": 5,
#     "Petka": 8,
#     "Oncike": 10,
#     "Zmoga": 6,
# }
# for vardas, pasiekimai in studziai.items():
#     print(vardas, pasiekimai)

# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius.
# Naudojant "while" ciklą, pridėkite kiekvieną įvestą skaičių prie sąrašo.
# Ciklą nutraukite, kai vartotojas įveda 0.

# Ivestis = []
# while True:
#     vesk = int(input("Įvesk skaičių (jei nori baigti, įvesk 0) "))
#     if vesk == 0:
#         break
#     else:
#         Ivestis.append(vesk)
# print(Ivestis)

# pateikimui



# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos.
# Vartotojas įveda gėrimo pavadinimą, o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne.
# Jei taip, išveskite jo kainą; jei ne, išveskite pranešimą "Gėrimas nerastas".

# gėrimai = {
#     "Fanta": 2.5,
#     "Vytautas": 1.5,
#     "Regal": 45
# }
# vesk = str(input("Įveskite gėrimo pavadinima "))
# if vesk in gėrimai:
#     kaina = gėrimai[vesk]
#     print("tokį gėrimą turime, jo kaina ", kaina)
# else:
#     print("tokio gėrimo neturim")

# 5. Patikrinkite, ar skaičiai sąraše yra lyginiai arba nelyginiai.
# ukurkite du tuščius sąrašus: vienas lyginiams ir kitą nelyginiams skaičiams,
# išrūšiuokite lyginius ir nelyginius skaičius iš skaičiai sąrašo.

# skaiciai = [2, 5, 7, 10, -1, 6, 8, 0]
# lyginiai = []
# nelyginiai = []
# for skaicius in skaiciai:
#     if skaicius %2 ==0:
#         lyginiai.append(skaicius)
#     else:
#         nelyginiai.append(skaicius)
# print("lyginiai ", lyginiai)
# print("nelyginiai ", nelyginiai)