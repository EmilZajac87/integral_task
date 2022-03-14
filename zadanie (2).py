import numpy as np
import math
import matplotlib.pyplot as plt
def calka(fun, zakres1,zakres2,ilosc):
    dzielenie = np.linspace(zakres1,zakres2,ilosc)
    szerokosc = dzielenie[1]-dzielenie[0]
    calka = 0
    for x in range(ilosc):
        x = x * szerokosc + zakres1
        calka += szerokosc * eval(fun)
    
    return calka
def calka_dolna_granica(zakres_p,zakres_k,funkcja,ilosc):
    szerokosc = (zakres_k-zakres_p)/ilosc
    calka_dolna = 0
    for i in range(ilosc-1):
        x = zakres_p
        yy = eval(funkcja)
        calka_dolna += yy*szerokosc
        zakres_p += szerokosc
    return calka_dolna
def calka_gorna_granica(zakres_p,zakres_k,funkcja,ilosc):
    szerokosc = (zakres_k-zakres_p)/ilosc
    calka_gorna = 0
    zakres_p += szerokosc
    for x in range(ilosc):
        x = zakres_p + szerokosc
        yy = eval(funkcja)
        calka_gorna += yy*szerokosc
        zakres_p += szerokosc
    return calka_gorna

funkcja = "x+2"
zakres_p = 1
zakres_k = 4
ilosc_prostokatow = 10
calki_przedzial = []
akceptowalny_blad = 0.01
i = True
granica_calki_dolnej = calka_dolna_granica(zakres_p,zakres_k,funkcja,ilosc_prostokatow)
granica_calki_gornej = calka_gorna_granica(zakres_p,zakres_k,funkcja,ilosc_prostokatow)
blad_calki = granica_calki_gornej - granica_calki_dolnej 
calka_przed = calka(funkcja,zakres_p,zakres_k,ilosc_prostokatow)
print(f"Całka przed przybliżeniem wynosi: {calka_przed}")
while i:
    if blad_calki>akceptowalny_blad:
        ilosc_prostokatow += 50
        granica_calki_dolnej = calka_dolna_granica(zakres_p,zakres_k,funkcja,ilosc_prostokatow)
        granica_calki_gornej = calka_gorna_granica(zakres_p,zakres_k,funkcja,ilosc_prostokatow)
        blad_calki = blad_calki = granica_calki_gornej - granica_calki_dolnej 
        
    else:
        i = False
        
calka = calka(funkcja,zakres_p,zakres_k,ilosc_prostokatow)
print(f"Wartość całki w zakresie [{zakres_p},{zakres_k}] funkcji {funkcja} i akceptowalnym bledzie {akceptowalny_blad} wynosi: {calka}")
print(f"Ilość przedziałów wynosi: {ilosc_prostokatow}")
print(f"Warość granicy dolnej to: {granica_calki_dolnej}")
print(f"Warość granicy gornej to: {granica_calki_gornej}")
print(f"Warość roznicy wynosi: {blad_calki}")


