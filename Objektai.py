# # sukuriame klase
#
# class Zmogus:
#     # sukuriamas konstruktorius
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#     # kuriami metodai
#     def sveikinimas(self):
#         return f"Sveiki, as esu {self.vardas} ir man yra {self.amzius} metu"
#
# # sukuriamas objektas
#
# zmogus1 = Zmogus("Migle", 30)
# zmogus2 = Zmogus("Antanas", 45)
# print(zmogus1.sveikinimas())
# print(zmogus2.sveikinimas())

# class Automobilis:
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#         self.greitis = 0
#     def akseleratorius(self):
#         self.greitis += 10
#
#     def stabdis(self):
#         self.greitis -= 5
#
#     def info(self):
#         return f"{self.marke} {self.modelis}, greitis: {self.greitis} km/h"
#
# auto1 = Automobilis("Mazda", "323")
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.akseleratorius()
# auto1.stabdis()
# print(auto1.info())

# class Knyga:
#     def __init__(self, pavadinimas, autorius, leidimo_metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.leidimo_metai = leidimo_metai
#     def info(self):
#         return f"Knygos pavadinimas {self.pavadinimas}, autorius: {self.autorius}, išleidimo metai: {self.leidimo_metai}"
#
# knyga1 = Knyga("'Visi norėjo testo'", "studentas", 2023)
# print(knyga1.info())


# class Preke:
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#     def info(self):
#         return f"{self.pavadinimas}: {self.kaina} eurų"
#
# class Krepselis:
#     def __init__(self):
#         self.prekes = []
#
#     def ideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def krepselio_info(self):
#         if not self.prekes:
#             print("Krepšelis tuščias")
#         else:
#             print("Krepšelyje yra: ")
#             for preke in self.prekes:
#                 print(preke.info())
#     def mokėtina_suma(self):
#         suma = sum(preke.kaina for preke in self.prekes)
#         return suma
#
# krepsys = Krepselis()
# preke1 = Preke("kokosas", 5.0)
# preke2 = Preke("Litras", 5.2)
# preke3 = Preke("sasyskos", 1.2)
# preke4 = Preke("Alus", 2.5)
#
# krepsys.ideti_preke(preke1)
# krepsys.ideti_preke(preke2)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke4)
#
# krepsys.krepselio_info()
#
# print(f"Bendra suma {krepsys.mokėtina_suma()} eurų")

# Sukurkite klasę "Saskaita", kuri turėtų šias savybes ir metodus:
#
#     * saskaitos_nr: sąskaitos numeris.
#     * balansas: sąskaitos balansas (numatytasis pradžioje yra 0).
#     * inesti(suma): metodas, kuris prideda nurodytą sumą prie sąskaitos balanso.
#     * isimti(suma): metodas, kuris sumažina sąskaitos balansą nurodyta suma, jei yra pakankamai lėšų,
# arba išveda pranešimą apie nepakankamą balansą.
#     * informacija(): metodas, kuris grąžina informaciją apie sąskaitą (sąskaitos numeris ir balansas).
#
# Sukurkite bent du objektus pagal šią klasę ir atlikite operacijas, tokiu kaip lėšų įnešimas ir išėmimas,
# bei gaukite sąskaitos informaciją.

# class Sąskaita:
#     def __init__(self, sąsk_nr, balansas=0):
#         self.sąsk_nr = sąsk_nr
#         self.balansas = balansas
#     def inesimas(self, suma):
#         if suma > 0:
#             self.balansas += suma
#         else:
#             print("neigiamos sumos neįnešam")
#     def išėmimas(self, suma):
#         if suma > 0 and self.balansas >= suma:
#             self.balansas -= suma
#         else:
#             print("čia tau ne sekundes bankas, - tiek eurų nėra // negalima išimti neigiamos sumos")
#     def sąsk_info(self):
#         return f"Sąskaitos numerio {self.sąsk_nr} balansas yra {self.balansas}"
# sask1 = Sąskaita("LT112")
# print(sask1.sąsk_info())
# sask2 = Sąskaita("USA911")
# print(sask2.sąsk_info())
# sask1.išėmimas(100)
# print(sask1.sąsk_info())
# sask1.inesimas(200)
# print(sask1.sąsk_info())
# sask1.išėmimas(100)
# print(sask1.sąsk_info())






