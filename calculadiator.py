# Calculation problems for kids

import random

def plús(a, b):
    s = svar()
    resault = a + b
    if s == resault:
        print(f"Vel gert rétta svarið var: {resault}")
        return True
    else:
        print(f"Rangt svar! Rétt svar var: {resault}")
        return False

def mínus(a, b):
    s = svar()
    resault = a - b
    if s == resault:
        print(f"Vel gert rétta svarið var: {resault}")
        return True
    else:
        print(f"Rangt svar! Rétt svar var: {resault}")
        return False

def deiling(a, b):
    s = svar()
    resault = a // b
    if s == resault:
        print(f"Vel gert rétta svarið var: {resault}")
        return True
    else:
        print(f"Rangt svar! Rétt svar var: {resault}")
        return False

def margföldun(a, b):
    s = svar()
    resault = a * b
    if s == resault:
        print(f"Vel gert rétta svarið var: {resault}")
        return True
    else:
        print(f"Rangt svar! Rétt svar var: {resault}")
        return False
def svar():
    return int(input("Svar: "))

def main():
    teljari = 1
    x = 0
    z = 0
    while teljari < 11:
        print(f"Dæmi {teljari}")
        if byrja == "+":
            t1 = 1
            t2 = 100
            t3 = 1
            t4 = 100
            tala_1 = random.randint(t1, t2)
            tala_2 = random.randint(t3, t4)
            print(f"Hvað er {tala_1} plús {tala_2}")
            samasem = plús(tala_1, tala_2)
        elif byrja == "-":
            t1 = 50
            t2 = 100
            t3 = 1
            t4 = 50
            tala_1 = random.randint(t1, t2)
            tala_2 = random.randint(t3, t4)
            print(f"Hvað er {tala_1} mínus {tala_2}")
            samasem = mínus(tala_1, tala_2)
        elif byrja == "*":
            t1 = 1
            t2 = 10
            t3 = 1
            t4 = 11
            tala_1 = random.randint(t1, t2)
            tala_2 = random.randint(t3, t4)
            print(f"Hvað er {tala_1} sinnum {tala_2}")
            samasem = margföldun(tala_1, tala_2)
        elif byrja == "/":
            q = 1
            while q != 0:
                t1 = 4
                t2 = 50
                t3 = 2
                t4 = 4
                tala_1 = random.randint(t1, t2)
                tala_2 = random.randint(t3, t4)
                q = tala_1 % tala_2
                if q == 0:
                    print(f"Hvað er {tala_1} deilt með {tala_2}")
                    samasem = deiling(tala_1, tala_2)
        else:
            print("OKAY")
        if samasem:
            x += 1
        else:
            z += 1
        teljari += 1
        print(f"Rétt svör {x}\nRöng svör {z}")
    if z == 0:
        print(f"TIL HAMINGJU! VEL GERT! Þú ert með {x} í einkunn.")
    elif x == 0:
        print(f"Heyrðu! Þú þarft að taka þig á og reikna meira og oftar! Einkunnin þín er {x}.")
    else:
        print(f"Þú ert með {x} í einkunn. Þú varst dreginn niður um {z} vegna rangra svara.")
        
# while byrja == True: # 1.skref - val notanda
#    try:    
byrja = input("Hæ hæ velkomin í stærðfræði. Ýttu á + - * eða / til að byrja.")
if byrja == "+" or "-" or "*" or "/":
    main()
#    except:
#        print("Innsláttarvilla! Þú verður að velja + eða - eða * eða / til að halda áfram.")