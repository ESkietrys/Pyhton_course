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

# Sukurkite klasę "Studentas", kuri turėtų šias savybes:
#
#     * vardas: studento vardas.
#     * pazymiai: sąrašas su studento pažymiais.
#
# Sukurkite klasę "Mokytojas", kuri turėtų šias savybes:
#
#     * vardas: mokytojo vardas.
#     * Mokytojo dėstoma tema: mokytojo dėstomas dalykas.
#
# Papildykite "Studentas" klasę metodu vidurkis(), kuris apskaičiuoja studento pažymių vidurkį.
#
# Papildykite "Mokytojas" klasę metodu ivertinimas(studentas, pazymys), kuris prideda studentui pažymį.
#
# Sukurkite objektus pagal "Studentas" ir "Mokytojas" klases,
# pridėkite pažymius ir vykdykite vidurkio apskaičiavimus bei pažymių pridėjimus.


# class Studentas:
#     def __init__(self, svardas):
#         self.svardas = svardas
#         self.pazymiai = []
#
#     def prid_paz(self, pazymys):
#         self.pazymiai.append(pazymys)
#
#     def MVid(self):
#         if not self.pazymiai:
#             return 0
#         return
#         suma = sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mvardas, dalykas):
#         self.mvardas = mvardas
#         self.dalykas = dalykas
#
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prid_paz(pazymys)
#
# studentas1 = Studentas("Tonis")
# mokytojas1 = Mokytojas("Juozas", "Nosiakrapščio pagrindai")
#
# mokytojas1.ivertinimas(studentas1, 9)
# print(f"{studentas1.svardas} vidurkis {studentas1.MVid()}")

# pasi=i8r4ti ir sulyginti
# class Studentas:
#     def __init__(self, st_vardas):
#         self.st_vardas = st_vardas
#         self.pazymiai = []
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, mokytojo_vardas, destomas_dakykas):
#         self.mokytojo_vardas = mokytojo_vardas
#         self.destomas_dalykas = destomas_dakykas
#     def ivertinimas(self, studentas, pazymys):
#         studentas.prideti_pazymi(pazymys)
#
# studentas1=Studentas('Petras')
# mokytojas1=Mokytojas('Jurgis', 'informatika')
#
# mokytojas1.ivertinimas(studentas1, 3)
#
# print(f'{studentas1.st_vardas}, vidurkis: {studentas1.vidurkis()}')


# Sukurkite klasę "Kava", kuri turėtų savybes "pavadinimas", "kaina", ir "talpa".
# Parašykite metodą, kuris patikrintų, ar ši kava yra tinkama tam tikram puodeliui, pagal jo talpą.

# class Kava:
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#
#     def tara(self, podTalpa):
#         if self.talpa <= podTalpa:
#             return f'{self.pavadinimas} kava tinka puodeliui su talpa {podTalpa} ml'
#         else:
#             return f'{self.pavadinimas} kava netinka puodeliui su talpa {podTalpa} ml'
#
# kava1 = Kava("juoda", 2.99, 250)
# puodelis1 = 300
# print(kava1.tara(puodelis1))

# klas4 knygynas, kuri turi savyb3 knygos (sarasas). prid4ti knnyga, ie6koti ir atspausdinti visu knygu sarasa :)
#
# class Knygynas:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#
#     def ieskok(self, pavadinimas):
#         for knyga in self.knygos:
#             if knyga["pavadinimas"] == pavadinimas:
#                 return knyga
#         return None
#
#     def sarasas(self):
#         if not self.knygos:
#             print("knygynas tuščias")
#         else:
#             print("Knygyno knygu sarasas: ")
#             for knyga in self.knygos:
#                 print(f"pavadinimas: {knyga['pavadinimas']} , autorius: {knyga['autorius']}. "Leidimo metai: {knyga["metai"]}})"
# knygynas = Knygynas()
# knygynas.prideti_knyga({'pavadinimas': "seselis", "autorius": "zemaitis", "metai": 1981})
# ieskok1 = knygynas.ieskok("seselis")
# if ieskok1:
#     print(f'rasta knyga: {ieskok1["pavadinimas"]}')
# else:
#     print("knygos n4ra, ateik po met7")
# knygynas.sarasas()

# surask klaidą

# class Knigynas: #susitvarkyti
# def __init__(self):
#     self.knygos = []
#
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#
#     def knygos_paieska(self, pavadinimas):
#         for knyga in self.knygos:
#             if knyga['pavadinimas'] == pavadinimas:
#                 return knyga
#             return None
#
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print("Knigynas tuscias")
#             else:
#             print('Knigyno knygu sarasas:')
#             for knyga in self.knygos:
#                                 print(
#                                     f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}")
#
#                 knigynas = Knigynas()
#                 knigynas.prideti_knyga({'pavadinimas': 'seslis', 'autorius': 'Zemaitis', 'metai': 1981})
#                 knigynas.prideti_knyga({'pavadinimas': 'soslis', 'autorius': 'femaitis', 'metai': 1881})
#                 ieskoma_knyga = knigynas.knygos_paieska('suslis')
#                 if ieskoma_knyga:
#                     print(f'rasta knyga: {ieskoma_knyga["pavadinimas"]}')
#                 else:
#                     print("knyga nerasta")
#                 knigynas.knygu_sarasas()


# Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
# Parašykite metodus, kurie leidžia pridėti prekes prie prekių sąrašo,
# pašalinti prekes ir paskaičiuoti prekių bendrą sumą;
#
# class Prekybininkas: #neveikia
#     def __init__(self, vardas):
#         self.vardas = vardas
#         self.prekes = []
#
#     def prideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def isimti_preke(self, preke): #papildonau for'as reikalingas
#         self.prekes.remove(preke)
#
#     def prekiu_suma(self, suma=0):
#         self.prekiu_suma = len(Prekybininkas.prekes)
#         if not self.prekes:
#             print("Sarasas tuscias")
#         else:
#             return
#
#
# prekybininkas1 = Prekybininkas("vardas": "Petka")
# prekybininkas1.prideti_preke({"preke": "oblius"})
#
# prekybininkas2.prideti_preke({"vardas": "plaktukas"})
#
# print(Prekybininkas.prekiu_suma)

#
# 3. Sukurkite klasę "Skaičiuotuvas", kuri turi metodus
# "sudėti" (add), "atimti" (subtract), "dauginti" (multiply) ir "dalinti" (divide).
# Šie metodai priima du skaičius ir atlieka atitinkamą matematinę operaciją.

# class Skaiciuotuvas:
#     def sudetis(self, sk1, sk2):
#         return sk1 + sk2
#     def atimtis(self, sk1, sk2):
#         return sk1 - sk2
#     def daugyba(self, sk1, sk2):
#         return sk1 * sk2
#     def dalyba(self, sk1, sk2):
#         if sk2 != 0:
#             return sk1 / sk2
#         else:
#             return ("dalyba iš nulio negalima")
#
# skaiciuotuvas = Skaiciuotuvas()
# print("Sudėtis:", skaiciuotuvas.sudetis(14, 2))
# print("Atimtis:", skaiciuotuvas.atimtis(14, 2))
# print("Daugyba:", skaiciuotuvas.daugyba(14, 2))
# print("Dalyba:", skaiciuotuvas.dalyba(14, 2))
# print("Dalyba2:", skaiciuotuvas.dalyba(14, 0))


# class Skaiciuotuvas:
#     def sudeti(self, skaicius1, skaicius2):
#         return skaicius1 + skaicius2
#
#     def atimti(self, skaicius1, skaicius2):
#         return skaicius1 - skaicius2
#
#     def dauginti(self, skaicius1, skaicius2):
#         return skaicius1 * skaicius2
#
#     def dalinti(self, skaicius1, skaicius2):
#         if skaicius2 == 0:
#             return "Dalyba iš nulio negalima"
#         return skaicius1 / skaicius2
#
# # Sukuriamas skaičiuotuvo objektas
# skaičiuotuvas = Skaiciuotuvas()
#
# # Atliktos matematinės operacijos
# suma = skaičiuotuvas.sudeti(5, 3)
# skirtumas = skaičiuotuvas.atimti(10, 4)
# sandauga = skaičiuotuvas.dauginti(6, 7)
# dalyba = skaičiuotuvas.dalinti(8, 0)
#
# # Išspausdinami rezultatai
# print(f"Sudėties rezultatas: {suma}")
# print(f"Atimties rezultatas: {skirtumas}")
# print(f"Daugybos rezultatas: {sandauga}")
# print(f"Dalybos rezultatas: {dalyba}")

#Sukurkite klasę "Darbuotojas" (Employee), kuri turi atributus
# "vardas" (name), "pareigos" (position), ir "atlyginimas" (salary).
# Parašykite metodus, kurie leidžia keisti darbuotojo pareigas ir atlyginimą;


# class Darbuotojas:
#     def __init__(self, vardas, pareigos, atlyginimas):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas
#
#     def keisti_pareigas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
#
#     def keisti_atlyginima(self, naujas_atlyginimas):
#         self.atlyginimas = naujas_atlyginimas
#
# darbuotojas1 = Darbuotojas("Jonas", "Kavos darytojas", 800)
# darbuotojas1.keisti_pareigas("Vakarėlių liūtas")
# darbuotojas2 = Darbuotojas("Petras", "Etatinis užknisinėtojas", 1500)
# darbuotojas2.keisti_atlyginima(200)
# print(f"Darbuotojo {darbuotojas1.vardas} naujos pareigos yra {darbuotojas1.pareigos}")
# print(f"Darbuotojo {darbuotojas2.vardas} naujas atlyginimas yra {darbuotojas2.atlyginimas}")

# Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
# Parašykite metodus, kurie leidžia pridėti prekes prie prekių sąrašo, pašalinti prekes
# ir paskaičiuoti prekių bendrą sumą;
#
# class Prekybininkas:
#     def __init__(self, vardas):
#         self.prekes = []
#
#     def prideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def pasalinti_preke(self, preke):
#         if preke in self.prekes:
#             self.prekes.remove(preke)
#             # alternatyva:
#         #
#         else:
#             print(f"{preke} nėra prekių saraše.")
#
#     def prekiu_suma(self):
#         return len(self.prekes)
#
# prekybininkas1 = Prekybininkas("Jonis")
# prekybininkas1.prideti_preke("Humusas")
# prekybininkas1.prideti_preke("Tonusas")
# prekybininkas1.prideti_preke("Kuskusas")
#
# prek_sum = prekybininkas1.prekiu_suma()
# print(prek_sum)
#
# prekybininkas1.pasalinti_preke("Humusas")
# prekybininkas1.pasalinti_preke("Antonusas")
# prek_sum = prekybininkas1.prekiu_suma()
# print(prek_sum)

# # Keista alternatyva

# class Prekybininkas:
#     def __init__(self, name):
#         self.name = name
#         self.prekes = []
#     def prideti_preke(self, preke, kiekis=1):
#         for _ in range(kiekis):
#             self.prekes.append(preke)
#     def pasalinti_preke(self, preke, kiekis=1):
#         if preke in self.prekes:
#            for _ in range(kiekis):
#                self.prekes.remove(preke)
#         else:
#             print("tokios prekes nera")
#
#     def prekiu_suma(self):
#         suma=sum(preke[1] for preke in self.prekes)
#         return suma
#
#
# pardavejas=Prekybininkas("Martynas")
# preke1=("kava", 1.0)
# preke2=("sultys", 2.5)
# preke3=("alus", 1.5)
#
# pardavejas.prideti_preke(preke1, 3)
# pardavejas.prideti_preke(preke2)
# pardavejas.prideti_preke(preke3,3)
# suma=pardavejas.prekiu_suma()
#
# print(suma)
#
# pardavejas.pasalinti_preke(preke1, 2)
# pardavejas.pasalinti_preke("preke4")
# suma=pardavejas.prekiu_suma()
#
# print("prekiu sarasas: ")
# for preke in pardavejas.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"bendra visu prekiu suma:{suma}")

# Sukurkite klasę "Klase", kuri turės savybę "pavadinimas" ir sąrašą "pamokos" (pamokų pavadinimai ir laikas).
# Sukurkite klasę "Mokykla", kuri turės sąrašą klasių.
# Parašykite metodą, kuris išveda mokyklos tvarkaraštį su visomis pamokomis.
#
# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.pamokos = []
#
#     def sukurti_pamoka(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#
#     def tvarkarastis(self):
#         tvarkarastis = f"Klase: {self.pavadinimas} \n"
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis += f"- {pavadinimas}, laikas: {laikas} \n"
#         return tvarkarastis
#
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#
#     def sukurti_klase(self, klase):
#         self.klases.append(klase)
#
#     def Tvarkarastis_galutinis(self):
#         galutinis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis += klase.tvarkarastis()
#         return galutinis
#
#
#
# klase1 = Klase("Ziopliu 9A")
# klase1.sukurti_pamoka("Nosiakrap6tis", "8:00-8:45")
# klase1.sukurti_pamoka("Kalbagrauzis", "9:00-9:45")
#
# klase2 = Klase("Smalsučiai gudručiai 1B")
# klase2.sukurti_pamoka("Priešpiečiai", "10:00-10:45")
# klase2.sukurti_pamoka("Kalbagrauzis", "11:00-11:45")
#
# mokykla =Mokykla("Tinginių pantys")
#
# mokykla.sukurti_klase(klase1)
# mokykla.sukurti_klase(klase2)
#
# tvarkarastis = mokykla.Tvarkarastis_galutinis()
#
# print(mokykla.Tvarkarastis_galutinis())

# Sukurkite klasę "Žaislas", kuri turėtų savybes, tokias kaip "pavadinimas" ir "amžiaus rekomendacija".
# Tada sukurkite klasę "Vaikas", kuri turėtų vardą ir amžių.
# Tada sukurkite klasę "VaikasSuZaislu", kuri turėtų šio vaiko objektą ir žaislo objektą.
# Patikrinkite, ar vaiko amžius atitinka žaislo amžiaus rekomendaciją.


# class zaislas:
#     def __init__(self, pavadinimas, amz_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amz_rekomendacija = amz_rekomendacija
#
# class vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
# class VaikasSuZaislu:
#     def __init__(self, zaislas, vaikas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#
#
#     def tikrinam_amziaus_zaisto_suderinamuma(self):
#         if self.vaikas.amzius >= self.zaislas.amz_rekomendacija:
#             return f"{self.vaikas.vardas} gali zaisti su žaisu " {self.zaislas.pavadinimas}
#         else:
#             return "atimkit is vaiko zaisla"
#
# zaislas1 = zaislas("lego", 3)
# zaislas2 = zaislas("lego1", 0.5)
# zaislas3 = zaislas("lego2", 10)
#
# vaikas1 = vaikas("jonas", 3)
# vaikas2 = vaikas("petras", 5)
# vaikas3 = vaikas("Onute", 11)
#
# vaikas_su_zaislu1 = VaikasSuZaislu(vaikas1, zaislas1)
#
# rezultatas = vaikas_su_zaislu1.tikrinam_amziaus_zaisto_suderinamuma()
# print(rezultatas)

# class Zaislas:
#     def __init__(self,pavadinimas, amziaus_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amziaus_rekomendacija = amziaus_rekomendacija
#
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius =amzius
#
# class VaikasSuZaislu:
#     def __init__(self,vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#     def amziaus_tikrinimas(self):
#         if self.vaikas.amzius >=self.zaislas.amziaus_rekomendacija:
#             return f'{self.vaikas.vardas} gali zaisti su zaislu "{self.zaislas.pavadinimas}" '
#         else:
#             return f'{self.vaikas.vardas} negali zaisti su zaislu "{self.zaislas.pavadinimas}", nes turi paaugti '
#
#
# zaislas1=Zaislas('Lego Betmen', 7)
# zaislas2=Zaislas('burbulai', 15)
# zaislas3=Zaislas('knyga', 8)
#
# vaikas1=Vaikas('Austeja',9)
# vaikas2=Vaikas('Eidvile', 0.5)
# vaikas3=Vaikas('Giedrius', 5)

# vaikas_su_zaislu1=VaikasSuZaislu(vaikas1, zaislas2)
#
# rezultatas = vaikas_su_zaislu1.amziaus_tikrinimas()
# print(rezultatas)


# Sukurkite programą, kuri leidžia vartotojui valdyti krepšinio komandą.
# Galite kurti klases, pvz., "Komanda", "Žaidėjas", "Treneris".
# Kiekvienas žaidėjas turėtų turėti savo statistiką (taiklumas,pozicija),
# o treneris - instrukcijas ir strategiją (komandos sudeti).
# Programa turi leisti vartotojui pridėti naujus žaidėjus, juos treniruoti ir valdyti komandos sudeti.
#
# class Komanda:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.zaidejai = []
#         self.treneris = Treneris()
#
# class Zaidejas:
#     def __init__(self, vardas, pozicija):
#         self.vardas = vardas
#         self.pozicija = pozicija
#         self.taiklumas = 30
#
#     def upgrade(self):
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#
#     def zaidejo_info(self):
#         return f"{self.vardas}, zaidejo pozicija {self.pozicija}, taiklumas (proc.) {self.taiklumas}"
#
#
#
# class Treneris:
#     def __init__(self, strategija, strategija_sudetis):
#         self.startegija = "ataka"
#
#     def keisti_strategija(self, nauja_strategija):
#         self.startegija = nauja_strategija
#
#     def strategijos_info(self):
#         return f"naudojama strategija {self.startegija}"
#
#     def prideti_zaideja(self, zaidejas):
#         self.zaidejai.append(zaidejas)
#     def isimti_zaideja(self, zaidejas):
#         self.zaidejai.remove(zaidejas)
#
#
#
# komanda1 = Komanda("Juoda_Balta ir vis tiek... ")
# zaidejas1 = Zaidejas("tolis", "ranksluosciu padavejas")
# zaidejas2 = Zaidejas("molis", "palei kase trinasi")
# zaidejas3 = Zaidejas("Metis", "meta ir nepataiko")
#
# komanda1.prideti_zaideja(zaidejas1)
# komanda1.prideti_zaideja(zaidejas2)
# komanda1.prideti_zaideja(zaidejas3)
#
# zaidejas1.upgrade()
# zaidejas2.upgrade()
# zaidejas3.upgrade()
#
# komanda.self_zaidejai

# class Treneris:
#     def __init__(self):
#         self.strategija = "ataka"
#     def keisti_strategija(self,nauja_strategija):
#         self.strategija = nauja_strategija
#
#     def strategijos_info(self):
#         return f'naudojama strategija {self.strategija}'
# class Zaidejas:
#     def __init__(self, pavarde, pozicija):
#         self.pavarde = pavarde
#         self.taiklumas = 30
#         self.pozicija = pozicija
#
#     def upgrade(self):
#         self.taiklumas += 5
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#
#     def zaidejo_info(self):
#         return f'{self.pavarde}, zaidejo pozicija {self.pozicija}, ir jo taiklumas {self.taiklumas}%'
# class Komanda:
#     def __init__(self, pavadinimas):
#         self.komanda =[]
#         self.pavadinimas = pavadinimas
#         self.treneris = Treneris()
#     def prideti_zaideja(self,zaidejas):
#         self.komanda.append(zaidejas)
#
#     def isimti_zaideja(self, zaidejas):
#         if zaidejas in self.komanda:
#             self.komanda.remove(zaidejas)
#     def komandos_informacija(self):
#         print(f'{self.pavadinimas}, komandos zaidejai: ')
#         for zaidejas in self.komanda:
#             print(zaidejas.zaidejo_info())
#     def strategijos_info(self):
#         print (self.treneris.strategijos_info())
#
#     def pasirinkti_treneri(self, treneris):
#         self.komanda.append(treneris)
#
#     def pakeisti_treneri(self, treneris):
#         if treneris in self.komanda:
#             self.komanda.remove(treneris)
#
# komanda=Komanda("Puseles")
# zaidejas1=Zaidejas("Greitas", "puolejas")
# zaidejas2=Zaidejas("didelis", "saugas")
# zaidejas3=Zaidejas("vidutinis", "atsarginis")
#
# komanda.prideti_zaideja(zaidejas1)
# komanda.prideti_zaideja(zaidejas2)
# komanda.prideti_zaideja(zaidejas3)
#
# zaidejas1.upgrade()
# zaidejas1.upgrade()
# zaidejas3.upgrade()
#
# komanda.komandos_informacija()
# komanda.strategijos_info()





