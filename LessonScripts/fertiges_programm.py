import random

leben = 9
wörter = ["Pizza", "Braut", "Tante", "Sorge", "Otter", "Pferd"]

geheim_wort = random.choice(wörter)

verdeckt_wort = list("?????")

herz = u'\u2764'

wort_richtig_geraten = False

def aktu_verdeckt(buchstabe_geraten, geheime_wort, verdeckt_wort):
    index = 0
    while index < len(geheim_wort):
        if buchstabe_geraten == geheim_wort[index]:
            verdeckt_wort[index] = buchstabe_geraten
        index = index +1

while leben > 0:
    print(verdeckt_wort)
    print("Verbleibende Leben: "+herz * leben)
    raten = input("Rate einen Buchstaben oder das Wort: ")

    if raten == geheim_wort:
                  wort_richtig_geraten = True
                  break
    if raten in geheim_wort:
        aktu_verdeckt(raten, geheim_wort, verdeckt_wort)
    else:
        print("Falsch. Ein Leben weniger")
        leben = leben -1
        
        
if wort_richtig_geraten:
    print("Du hast gewonnen! Das Wort wart " + geheim_wort)
else:
    print("Leider verloren! Das Wort war " + geheim_wort)

        
