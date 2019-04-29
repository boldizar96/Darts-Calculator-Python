#importok
import sys
from jatekos import Jatekos
import os
import time
from hiba import TulSok
from hiba import HibasBemenet

clear = lambda: os.system('cls' if os.name=='nt' else 'clear') #terminál törlése parancs

jatek = True #amíg a "jatek" igaz, addig bent maradunk a while ciklusban, új játék kezdéséhez szükséges
while(jatek):
    #játéktípus kiválasztása
    jatekTipusWhile = True #amíg nem adtak meg létező játékot, addig igaz marad, azaz a while ciklusból nem lépünk addig ki
    jatekTipus = None #501 vagy 301 
    while(jatekTipusWhile):
        jatekTipusInput = input("501-es vagy 301-es játékot szeretnél játszani?\n(Írd be, hogy:\"501\" vagy \"301\", kilépés \"q\")\n")
        jatekTipusInput = jatekTipusInput.strip() #whitespace-k levágása
        if(jatekTipusInput == "501"):
            print("A kiválasztott játéktípus: 501")
            jatekTipus = int(jatekTipusInput)
            jatekTipusWhile = False
        elif(jatekTipusInput == "301"):
            print("A kiválasztott játéktípus: 301")
            jatekTipus = int(jatekTipusInput)
            jatekTipusWhile = False
        elif(jatekTipusInput == "q"):
            print("A program most kilép.")
            exit()
        else:
            print("Nincs ilyen típusú játék.")
            jatekTipusWhile = True
    clear()

    #játékosok számának megadása
    jatekosokSzamaWhile = True #amíg nem adtak meg játékosszámot, addig igaz marad, azaz addig a while ciklusban maradunk és kérjük az inputot játékosszámra
    jatekosokSzama = None #1-6-ig
    while(jatekosokSzamaWhile):
        jatekosokSzamaInput = input("Add meg, hogy hányan szeretnétek játszani!\n(1-6 játékos)\nkilépés \"q\"\n")
        jatekosokSzamaInput = jatekosokSzamaInput.strip()
        if(jatekosokSzamaInput == "Q" or jatekosokSzamaInput == "q"):
            print("A program most kilép.")
            exit()
        try:
            jatekosokSzama = int(jatekosokSzamaInput)
        except:
            print("Számot adj meg 1-től 6-ig!")
        if(jatekosokSzama>6 or jatekosokSzama < 1):
            print("1-től 6-ig adj meg számot!")
            jatekosokSzamaWhile = True
        else:
            print("Játékosok száma: {}\n".format(jatekosokSzama))
            jatekosokSzamaWhile = False
    clear()

    #kiszálló típusa
    kiszalloWhile = True #amíg nem adnak meg kiszálló típust, addig bekérjük az inputot
    kiszallo = None #szimpla(bármilyen nyíllal ki lehet szállni), dupla (csak dupla kiszálló)
    while(kiszalloWhile):
        kiszalloInput = input("Add meg, hogy szimpla vagy dupla kiszállós játékot szeretnél-e játszani!\n\"S\": szimpla, \"D\": dupla\nkilépés: \"q\"\n")
        kiszalloInput = kiszalloInput.strip() #whitespace törlés
        kiszalloInput = kiszalloInput.upper() #nagybetűssé tétel az egyértelműség miatt
        if(kiszalloInput == "S"):
            print("Szimpla kiszállós játékot választottál!")
            kiszallo = "szimpla"
            kiszalloWhile = False
        elif(kiszalloInput == "D"):
            print("Dupla kiszállós játékot választottál!")
            kiszallo = "dupla"
            kiszalloWhile = False
        elif(kiszalloInput == "Q"):
            print("A program most kilép.")
            exit()
        else:
            print("Hibás bemenet. Próbáld újra!")
            kiszalloWhile = True
    clear()

    #játékosok generálása
    print("Játékosok beállítása.")
    nevMegad = None #sorszámot kell-e generálni a játékosoknak (false) vagy majd a felhasználó begépeli (true)
    nevMegadWhile = True
    while(nevMegadWhile):
        nevMegadInput = input("Szeretnél a játékosoknak nevet adni, vagy sorszám elég?\n1 - név megadás\n2 - elég a sorszám(alapértelmezett\nenter - alapértelmezett\n\"q\" - kilépés\n")
        nevMegadInput = nevMegadInput.strip() #whitespace törlés
        nevMegadInput = nevMegadInput.upper() #nagybetűssé tétel egyértelműség miatt
        if(nevMegadInput == "" or nevMegadInput == "2"):
            nevMegad = False
            nevMegadWhile = False
        elif(nevMegadInput == "1"):
            nevMegad = True
            nevMegadWhile = False
        elif(nevMegadInput == "Q"):
            print("A program most kilép.")
            exit()
        else:
            print("Hibás bemenet! Próbáld újra!")
            nevMegadWhile = True
    clear()

    jatekosok = []
    if(nevMegad): #kézi névmegadás
        for i in range(jatekosokSzama):
            nev = input("Add meg a(z) {}. játékos nevét:".format(i+1))
            jatekosok.append(Jatekos(nev,jatekTipus))
    else: #játékosok nevei sorszámmal
        for i in range(jatekosokSzama):
            jatekosok.append(Jatekos("{}.játékos".format(i+1),jatekTipus))
    clear()

    #súgó
    def sugo():
        print("Pontok megadása:")
        print("T# - tripla")
        print("D# - dupla")
        print("# - szimpla")
        print("Megjegyzés: # = zóna értéke")
        print("BULL(kicsi) - 25")
        print("BULL(nagy) - 50")
        print("------------------------------")
        print("{} - {}".format(jatekTipus,kiszallo))
        print("------------------------------")

    nyert = False
    brekk = False
    while(not(nyert)): #amíg valaki nem nyert, addig játszunk
        clear() #terminál törlése minden kör elején
        sugo() #súgó kiírása
        brekk = False
        for i in range(jatekosokSzama): #játékosok nevei és pontjainak kiírása
            print("{} - {}".format(jatekosok[i].nev,jatekosok[i].pontok))
        print("------------------------------")
        for i in range(jatekosokSzama): #játékosok dobása sorban
            dobTovabb = True 
            db = 1 #nyíl számláló
            dobas1 = None #
            dobas2 = ""
            dobasok = 0 #aktuális játékos adott körben való dobásainak összegzője (túldobás esetén ezt az összeget kell a ponthoz (vissza)adni)
            if(brekk):
                break
            print("{}:".format(jatekosok[i].nev)) #írjuk ki, hogy ki dob
            if(kiszallo):
                jatekosok[i].kiszallo() #dupla kiszálló kiírása
            else:
                jatekosok[i].kiszallo2() #szimpla kiszálló kiírása
            while(dobTovabb and db < 4):                
                dobas1s = input(str(db) + ". nyíl: ") #bekérjük a dobás értékét a súgónak megfelelően
                dobas1s = dobas1s.strip() #whitespace törlés
                dobas1s = dobas1s.upper() #nagybetűssé alakítás az egyértelműsítés miatt
                if(len(dobas1s)>=1): #ha van bevitt karakter, akkor vizsgáljuk csak az inputot
                    if(dobas1s[0] == "T"): #ha az első karakter T
                        dobas1s = dobas1s[1:] #vágjuk le az első karaktert
                        try:
                            dobas1 = int(dobas1s) #inputot (dobást) alakítsuk át
                            if(dobas1 > 20 or dobas1 < 0 ): #20 felett és 0 alatt ne fogadjuk el a megadott adatokat
                                raise HibasBemenet()
                            dobas1 = 3 * dobas1 #tripla résznél vagyunk, ezért 3-szoros értékkel számulunk
                            dobasok = dobasok + dobas1 #kör dobásainak összegét növeljük az aktuális dobással
                            dobas2 = ""
                            if(kiszallo == "dupla"): #dupla kiszállózás esetén
                                dobas2 = jatekosok[i].dobD1(dobas1) #a duplás dobást használjuk
                            else: #szimpla kiszállózás esetén
                                dobas2 = jatekosok[i].dob(dobas1) #elég a sima dobás metódust használni
                            if(dobas2 == "hiba"): #ha hibával tér vissza valamelyik metódus
                                raise TulSok() #akkor túl sokat dobott a játékos
                            elif(dobas2 == "vege"): #ha végéval, akkor nyert az adott játékos
                                raise Exception()
                            db = db + 1 #ha ide eljutunk, akkor sikeres volt a dobás, növeljük az eldobott nyilak számát
                            print("{} - {}".format(jatekosok[i].nev,jatekosok[i].pontok)) #játékos nevének és pontjának kiírása a dobás végén
                        except HibasBemenet:
                            print("Hibás bemenet!")
                            sugo()
                            dobTovabb = True #hibás input volt, újra be kell kérni, így ez igaz marad
                        except TulSok:
                            print("Túl sokat dobtál...")
                            dobTovabb = False #túl sokat dobott, a kört be kell fejezni -> hamissá válik
                            jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1 #és ekkor a pontokat visszaadjuk
                        except: #játék vége
                            dobTovabb = False #játék vége, nincs több dobás
                    elif(dobas1s[0] == "D"): #ha az első karakter D
                        dobas1s = dobas1s[1:] #első karakter lemetszése
                        try:
                            dobas1 = int(dobas1s) #intté alakítjuk
                            if(dobas1 > 20 or dobas1 < 0): #ha 20-nál több van írva vagy 0-nál kevesebb, akkor hiba, mert nincs olyan zóna
                                raise HibasBemenet()
                            dobas1 = 2 * dobas1 #mivel DUPLA van megadva, ezért megkétszerezzük a D utáni szám értékét
                            dobasok = dobasok + dobas1 #ezt a kör dobásainak összegéhez adjuk
                            dobas2 = ""
                            if(kiszallo == "dupla"): #ha dupla kiszálló van, akkor
                                dobas2 = jatekosok[i].dobD2(dobas1) #a dupla kiszállós dobás szerint futtassuk a dobást
                            else: #ha szimpla kiszállós, akkor
                                dobas2 = jatekosok[i].dob(dobas1) #a szimpla kiszállós dobás metódust hívjuk
                            if(dobas2 == "hiba"): #ha hibával térünk vissza, akkor 
                                raise TulSok() #dobjunk tulsok exceptiont
                            elif(dobas2 == "vege"): #ha vége a játéknak
                                raise Exception() #akkor az ehhez kapcsolódó exceptiont
                            db = db + 1 #eldobott nyilak számát növeljük
                            print("{} - {}".format(jatekosok[i].nev,jatekosok[i].pontok)) #játékos nevének és pontjának kiírása a dobás végén
                        except HibasBemenet:
                            print("Hibás bemenet!")
                            sugo()
                            dobTovabb = True #adott nyilat kérjük be újra
                        except TulSok:
                            print("Túl sokat dobtál...")
                            dobTovabb = False #túl sokat dobott, kör vége
                            jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1
                        except: #játék vége
                            dobTovabb = False #játék vége, kör vége is
                    elif(dobas1s.isdigit()): #szimpla szám beolvasása
                        try:
                            dobas1 = int(dobas1s)
                            if(dobas1 > 20 and (dobas1 != 25 and dobas1 != 50)): #1-től 20-ig vannak zónák, plusz a BULL, ami 25 és 50; negatív értéket alapból hibás bemenetként fog érzékelni
                                raise HibasBemenet()
                            dobas1 = dobas1 #ez a sor elhagyható lenne
                            dobasok = dobasok + dobas1 #játékos körének dobásainak összegéhez hozzáadjuk az aktuális dobást
                            dobas2 = None
                            if(kiszallo == "dupla"): #dupla kiszálló esetén
                                if(dobas1 == 50): #a nagybull elfogadott kiszállónak
                                    dobas2 = jatekosok[i].dob(dobas1)
                                else: #illetve a dupla dobás is
                                    dobas2 = jatekosok[i].dobD1(dobas1)
                            else: #szimpla kiszálló esetén bármely dobás elfogadott kiszállónak
                                dobas2 = jatekosok[i].dob(dobas1)
                            if(dobas2 == "hiba"): #túldobás esetén túl sok hibát dobjunk
                                raise TulSok()
                            elif(dobas2 == "vege"): #jó kiszállózás esetén univerzális hibát dobjunk
                                raise Exception()
                            db = db + 1 #eldobott nyíl számláló növelése
                            print("{} - {}".format(jatekosok[i].nev,jatekosok[i].pontok)) #játékos nevének és pontjának kiírása a dobás végén
                        except HibasBemenet:
                            print("Hibás bemenet!")
                            sugo()
                            dobTovabb = True #rossz input esetén újre bekérjük
                        except TulSok:
                            print("Túl sokat dobtál...")
                            dobTovabb = False #túl sok dobás esetén a kör véget ér
                            jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1 #és a dobott pontokat vissza kell adni a pontokhoz
                        except: #játék vége
                            dobTovabb = False #ilyenkor is vége a körnek
                    else:
                        print("Hibás bemenet!")
                        sugo()
                        dobTovabb = True #mivel nem volt megfelelő input, ezért továbbra is be kell kérni a dobás értékét
                else: #dobás megadása helyett üres enter ütés kivédésére
                    print("Hibás bemenet!")
                    sugo()
                    dobTovabb = True #mivel nem dobott el nyilat (nem volt input), ezért továbbra is dobni kell
                if(db > 4):
                    dobTovabb = False #biztos ami biztos, ha a 4. nyíl jönne, akkor a továbbdobás lehetőségét kapcsoljuk ki
                if(jatekosok[i].nyert()): #ha valamelyik játékos nyert
                    print("{} nyert".format(jatekosok[i].nev)) #írjuk ki, hogy ki nyert
                    ujjatekWhile = True
                    while(ujjatekWhile):
                        ujjatek = input("Szeretnél új játékot kezdeni?\nI - Igen\nN - Nem\n")
                        ujjatek = ujjatek.strip()
                        ujjatek = ujjatek.upper()
                        #print(ujjatek)
                        if(ujjatek == "I"):
                            ujjatekWhile = False #jó input volt, nem kell többet bekérni
                            nyert = True #valaki nyert, ennek a játéknak vége
                            dobTovabb = False #játéknak vége van, nem dobunk tovább
                            brekk = True #break-eljük a dobásokat
                            jatek = True #játszunk még egyet, IGEN
                        elif(ujjatek == "N"):
                            ujjatekWhile = False #jó input volt, nem kell többet bekérni
                            nyert = True #valaki nyert, ennek a játéknak vége
                            dobTovabb = False #játéknak vége van, nem dobunk tovább
                            brekk = True #break-eljük a dobásokat
                            jatek = False #játszunk még egyet, NEM
                        else:
                            print("Hibás bemenet. Próbáld újra!")
                            ujjatekWhile = True #nem volt jó bemenet, kérdezzük meg újra
            print("------------------------------------")
        time.sleep(2) #kiírás végén várjunk 2 mp-et, hogy valamennyire leolvasható legyen a képernyő

print("A program most kilép.") #végül írjuk ki, hogy most kilépünk
exit() #és lépjünk ki