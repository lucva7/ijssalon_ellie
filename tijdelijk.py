prijzen = {
    'aardbei': 3,
    'vanille': 4,
    'chocolade': 5
}
aanbieding = 'vanille'
prijzen[aanbieding] *= 0.80
print(prijzen)
reclame_tekst = f"Vandaag in de aanbieding: Vanille-ijs, 1 liter - slechts €{prijzen[aanbieding]:.2f}"
reclame_tekst2 = reclame_tekst[:76]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    print(el)
for el in reclame_tekst4:
    print(el.lower())
for el in reclame_tekst4:
    if len(el) >=5:
        print(el.upper())
    else:
        print(el.lower())
