import math
import random


def fel1():
    print("feladatok:Kérj be 1 páros számot a felhasználótól. (1 pont)\n"
          "Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot,\n "
          "addig, amíg páros számot nem ad meg!  (1 pont)	")
    szam: int = int(input("Kérek egy számot!"))
    while not szam % 2 == 0:
        print("Ez nem páros!", end=" ")
        szam: int = int(input("Páros számot kérek!"))


def fel2():
    print("feladatok:2.Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot.\n"
          "Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”")
    db: int = 0
    i: int = 0
    while i < 15:
        szam: float = math.floor(random.random() * 141 + 10)
        if szam % 3 == 0:
            db += 1
        i += 1
    print(f"A szamok között {db} 3-mal osztható van!")


def fel3(szoveg: str, szam: int):
    print("feladat:Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot.\n "
          "Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!\n”"
          "Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! ")
    if len(szoveg) < szam:
        print(f"Nincs {szam}. karakter!")
    else:
        for i in range(3):
            print(f"{szoveg[szam-1].upper()}", end=" ")


def fel4():
    print("feladat:Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.\n"
          "Hány nevet adott meg a felhasználó?\n"
          "A kiírás formája: „A felhasználó 12 nevet adott meg.”")
    db: int = 0
    nev: str = input("Adjon egy nevet!(@ írjon ,hogy le álljon)")
    while nev != "@":
        db += 1
        nev: str = input("Adjon egy nevet!(@ írjon ,hogy le álljon)")
    print(f"A felhasználó {db} nevet adott meg.")


def fel5():
    print("feladat:Szimuláljuk a kő-papír-olló játékot.\n"
          "Írj eljárást, amiben:\n"
          "A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget,\n"
          " majd tárold el a felhasznalo_tippje változóban.\n"
          "Ezután a gép generál egy egész számot [1,3] között.\n"
          " 1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban\n"
          "Ezután írd ki, hogy ki nyert!\n"
          "Ha a két szó ugyanaz, írja ki, hogy Döntetlen.\n"
          "Egyéb esetben azt írja ki, aki győzött!\n"
          "++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!\n")
    tipp: str = input("Adjon meg egy tippet!(kő/papír/olló)")
    tipp.lower()
    while not ((tipp == "kő") or (tipp == "papír") or (tipp == "olló")):
        tipp: str = input("Adjon meg egy tippet!(kő/papír/olló)")
        tipp.lower()
    gepTipp: int = math.floor(random.random()*3+1)
    gepErtek = ""
    if gepTipp == 1:
        gepErtek = "kő"
    if gepTipp == 2:
        gepErtek = "papír"
    if gepTipp == 3:
        gepErtek = "olló"

    if tipp == gepErtek:
        print("Döntetlen")
    elif tipp == "kő" and gepErtek == "olló":
        print("Játékos nyert")
    elif tipp == "kő" and gepErtek == "papír":
        print("Gép nyert")
    elif tipp == "papír" and gepErtek == "kő":
        print("Játékos nyert")
    elif tipp == "papír" and gepErtek == "olló":
        print("Gép nyert")
    elif tipp == "olló" and gepErtek == "papír":
        print("Játékos nyert")
    elif tipp == "olló" and gepErtek == "kő":
        print("Gép nyert")




