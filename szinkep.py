#!/urs/bin/python3
# -*- coding:utf-8 -*-

"""2012.oktober.19 erettsegi megoldas Python Programozasi nyelven. """

""" 1. feladat"""
"""Adat beolvasas amit en egy szotarba gondoltam. Ami a kovetkezo keppen nezne ki:
kep={
szam(Hanyadik){
"R" = 200
"G" = 96
"B" = 64
"Egesz" = 200 96 64
 }
}
"""
kep = {}
n = 0
sorok = 1
oszlop  = 0
with open("kep.txt","rt+", encoding="utf-8") as f:
    for s in f:
        n+=1
        if oszlop == 50:
            sorok += 1
            oszlop = 0
        oszlop += 1
        sor = s.replace("\n", "").split(" ")
        kep[n] = {}
        kep[n]['R'] = int(sor[0])
        kep[n]['G'] = int(sor[1])
        kep[n]['B'] = int(sor[2])
        kep[n]['Egesz'] = [sor[0],sor[1],sor[2]]
        kep[n]['sor'] = sorok
        kep[n]['oszlop'] = oszlop 
        
#print(kep)

"""
A javitashoz egy ki segitseg.
with open('sem.txt', 'wt', encoding='utf-8') as g:
    for k, a in kep.items():
        g.write("{0}:{1} \n".format(k,a))

"""
print("2. feladat")
"""Be kell kerni egy RGB--kodot es meg kell vizsgalni hogy benne van-e a szotarban. """
r = int(input("Kerem adjon be a RGB kod voros \R\ osszetevojet."))
g = int(input("Kerem adjon be a RGB kod zold \G\ osszetevojet."))
b = int(input("Kerem adjon be a RGB kod kek \B\ osszetevojet."))
for a in kep.values():
    if a['R'] == r and a['G'] == g and a['B'] == b:
        print("Megtalalhato ez a szin a kepen.")
        break
    else:
        print("Sajnos nincsen ilyen szin a kepen.")
        break

print("3. feladat")
"""Meg kell hatarozni hogy a 35 sor 8 keppont szine hanyszor szerepel a 35--odik sorben es a 8 oszlopba."""

szam_oszlop = 0
szam_sor = 0
kep_RGB = []
for k in kep.values():
    if k['sor'] == 35 and k['oszlop'] == 8:
        kep_RGB = k['Egesz']

    if k['sor'] == 35 and k["Egesz"] == kep_RGB:
        szam_sor+=1

    if k['oszlop'] == 8 and k["Egesz"] == kep_RGB:
        szam_oszlop+=1

print("Sorban: {0} Oszlopban: {1}".format(szam_sor, szam_oszlop))

print("4. feladat")
"""Meg kell allapitani hogy a voros kek zold szin kozul melyik fordul elo legtobbszor. """
voros = 0
kek = 0
zold = 0
for a in kep.values():
    if a['Egesz'] == ['255', '0', '0']:
        voros+=1
    if a['Egesz'] == ['0', '255', '0']:
        kek+=1
    if a['Egesz'] == ['0', '0', '255']:
        zold+=1

szinek = [voros,kek,zold]
sz = sorted(szinek)
if sz[-1] == voros:
    print("szin: voros")
if sz[-1] == kek:
    print("szin: kek")
if sz[-1] == zold:
    print("szin: zold")


print("5. feladat")
"""Uj szotart kell kepezni es ki kell cserelni hogy 3 keppontos fekete keret legyen az egesz kepnek."""
keret = {}

for a, k in kep.items():
    fekete = [0, 0, 0]
    keret[a] = {}
    keret[a]["sor"] = k["sor"]
    keret[a]["oszlop"] = k["oszlop"]
    
    if k['sor'] == 1 or k['sor'] == 2 or k['sor'] == 3:
        keret[a]["Egesz"] = fekete
    elif k['oszlop'] == 1 or k['oszlop'] == 2 or k['oszlop'] == 3:
        keret[a]["Egesz"] = fekete
    elif k['sor'] == 48  or k['sor'] == 49 or k['sor'] == 50:
        keret[a]["Egesz"] = fekete
    elif k['oszlop'] == 48 or k['oszlop'] == 49 or k['oszlop'] == 50: 
        keret[a]["Egesz"] = fekete
    else:
        keret[a]["Egesz"] = k['Egesz']
#print(keret)

print("6. feladat")
"""Elozo feladat szotarat ki kell irni a keretes.txt--fajlba. """

with open('keretes.txt', 'wt', encoding='utf-8') as g:
    for a in keret.values():
        g.write("{0} \n".format(a["Egesz"]))


print("7. feladat")
"""Meghatarozni hol van sarga hol kezdodik es hol van a vege. """
sarga = []
for a in kep.values():
    if a['Egesz'] == ['255', '255', '0']:
        sarga.append(str(a['sor'])+", "+str(a['oszlop']))

ab = sarga[0].split(":")
aesb = ab[0].split(",")
cd = sarga[-1].split(":")
cesb = cd[0].split(",")
pixel = ((int(cesb[0])-int(aesb[0]))*(int(cesb[1])-int(aesb[1])))

print("Kezd: {0}, {1}".format(aesb[0], aesb[1]))
print("Vege: {0}, {1}".format(cesb[0], cesb[1]))
print("Keppont szama: {0}".format(pixel))

