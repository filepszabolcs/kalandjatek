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


    if i == 20:
        print("22. a nap hátralévő részében disznó vicceken röhögtök... \n"
              " Mit választasz? Írj be a számot:")
        v = int(input())
        if v == 22:
            i = v
