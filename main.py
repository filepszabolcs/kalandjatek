i = 1
while i != 19 or i != 22:
    if i == 1:
        print("Te vagy az iskola rosszfiúja. Késve érkezel a suli elé, még elszívod a cigidet, aztán… \n"
              "2. elnyomod a csikket az igazgatónő bringájának kerekébe. \n"
              "3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket. \n"
              "4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire. \n"
              "Mit választasz? Írj be a számot:")
        v = int(input())
        if v == 2 or v == 3 or v == 4:
            i = v

    if i == 2:
        print("észreveszi az éppen érkező töri tanárod, mit tettél és… \n"
              "5. azonnal felrángat az igazgatói irodába. Te hőzöngve tiltakozol végig a folyosón. \n"
              "6. gratulál neked, hisz szerinte is egy nagyképű szipirtyó a nő. \n"
              "7. szó nélkül tovább sétál, mivel eléggé parázik tőled. \n"
              "Mit választasz? Írj be a számot:")
        v = int(input())
        if v == 5 or v == 6 or v == 7:
            i = v

    if i == 3:
        print(
            "8. az akciód nem jól sül el, mivel az égő csikktől meggyullad a szemét és lángra kap az egész bejárati ajtó.\n"
            "9. a gondnok meghunyászkodva elkezdi összeseperni a szemetet.\n"
            "10. pechedre akkor ér oda melléd az a dögös csaj az évfolyamról, akinek szemlátomást nem jön be a viselkedésed. \n"
            "Mit választasz? Írj be a számot:")
        v = int(input())
        if v == 8 or v == 9 or v == 10:
            i = v

    if i == 4:
        print("11. Béci rávesz, hogy lógjátok el az egész napot. Belemész.\n"
              "12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.\n"
              "13. kiszúrod az éppen közeledő dögös csajt az évfolyamról és Béci megszólítja.\n"
              "Mit választasz? Írj be a számot:")

        v = int(input())
        if v == 11 or v == 12 or v == 13:
            i = v