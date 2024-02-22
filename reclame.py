def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs=prijs-(prijs*korting)
    aanbieding_tekst=f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro naar voor {nieuwe_prijs:.2f} euro."
    return aanbieding_tekst

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag:.2f} euro btw betaald moet worden."

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

def gemiddelde(mijn_lijst):
    gemiddelde_waarde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde:.2f} euro."

def hoog_en_laag(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [hoogste, laagste]

def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

def combinatie(invoer_lijst_2):
    from algemene_functies import invoer_lijst_2
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
