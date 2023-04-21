"If" ist erstmal ein englisches Wort und bedeutet "wenn". Das Wort "wenn" nutzen wir, um Bedingunen und sich daraus resultierende Folgen auszudrücken.

Beispiel? Wenn es morgen regnet, gehe ich nicht spazieren. Hier sieht man ganz deutlich: Ob ich spazieren gehe ist abhängig von der Bedingung, ob es morgen regnet. Und man sieht nocht mehr. Sollte das Wetter uns nämlich wohl gesonnen sein und strahlender Sonnenschein herrschen (oder es  zumindestens trocken sein und nicht regnen), dann werden wir spazieren gehen. In der Programmiersprache könnten wir dieses Beispiel dann formulieren mit:
```python
wetter = "regen"
if wetter == "regen":
    print("Ich gehe nicht spazieren")
else:
    print("Ich gehe spazieren")
```

Zwei Dinge bedürfen hier einer näheren Betrachtung. Zum einen fällt das Zeichen "==" ins Auge. Dieses ist ein sogenannter **Operator** und hat die Funktion, **die Gleichheit zweier Werte** zu testen. Sind die beiden angegeben Werte auf beiden Seiten des "==" gleich, so gibt der Operator 
```python
wetter == "regen"
```
den Wert *True* zurück, was ein englisches Wort ist und wahr bedeutet. Sind die Werte auf beiden Seiten des "==" Operators nicht gleich, so wird - man ahnt es schon - der Wert *False* zurückgegeben, was auf deutsch falsch bedeutet.

## Aufgabe
Geben die folgenden Werte den Ausdruck *True* oder *False* zurück? Stelle erst Vermutungen an und tippe sie dann in die Python IDLE ein und überprüfe die Rückgabe.
```python
True == True
True == False
3==2
"Hallo" == "Hallo" 
"Hallo" == "hallo"
3*2 == 2*3
```

Zum anderen fällt das Wort *else* auf. Dieses Wort bedeutet im deutschen *sonst*. Somit lautet der obere Programmierausdruck in nicht Programmiersprache übersetzt:

Wenn wetter gleich (==) "regen" ist (bzw. der Wert *True* zurückgegeben wird), dann gib "Ich gehe spazieren" auf der Konsole aus, sonst gib   "Ich gehe spazieren" auf der Konsole aus (was bedeutet, dass keine der Bedingungen erfüllt worden ist).

Aber wofür ist das nun gut?

Eine if-Abfrage lässt sich als **Verzweigungen** verstehen. **Verzweigungen** ermöglich es dabei, abhängig von Bedingungen unterschiedliche Codeteile auszuführen. Also in unserem Beispiel: Sollte es regnen, gehen wir nicht spazieren und sollte es regnen, gehen wir spazieren. In Python haben if-Verzweigungen folgenen Aufbau:
```python
if bedingung1:
    block1
elif bedingung2:
    block2
elif bedingung3:
    block3
else:
    block4
```
**Wichtig:** Sowohl **"elif"** als auch **"else"** sind optional. Das bedeutet, dass 
```python
if bedingung1:
    block1
```
auch ohne elif und else funktioniert.

Aber was ist nun *elif*? **Elif** steht für *else if* und meint soviel wie: "ansonsen wenn".

Beispiel:
```python
wetter = "regen"
if wetter == "regen":
    print("Ich gehe nicht spazieren")
elif wetter == "sonne":
    print("Ich gehe spazieren und nehme meine Sonnenbrille mit.")
else:
    print("Ich gehe spazieren")
```

Also übersetzt: Wenn wetter gleich (==) "regen" ist (bzw. der Wert *True* zurückgegeben wird), dann gib "Ich gehe spazieren" auf der Konsole aus, ansonsten wenn wetter gleich (==) "sonne" ist (bzw. auch hier der Wert *True* zurückgegeben wird), dann gib "Ich gehe spazieren und nehme meine Sonnenbrille mit" auf der Konsole aus, sonst gib  "Ich gehe spazieren" auf der Konsole aus (was bedeutet, dass keine der Bedingungen erfüllt worden ist).

## Aufgabe
Teste den oberen Code selber aus. Was wird ausgegeben. Wie ändert sich die Ausgabe des Codes, wenn du anstatt 
```python
wetter = "regen"
```

beispielsweise

```python 
wetter = "sonne"
```

eingibst.

## Aufgabe
1) Schreibe ein Programm, dass je nach Wetterlage verschiedene Sätze in der IDLE ausgibt. Dabei soll als erstes der Benutzer gefragt werden, wie das Wetter ist und der eingebene Wert in einer Variable abgelegt werden (input-Befehl). Daraufhin soll das Programm mittels einer if-Abfrage verschieden darauf reagieren.

2) Schreibe ein Gespräch zwischen Mensch und Computer, in dem der Computer auf die Eingabe des Menschen unterschiedlich reagiert. Bspw. könntest du wie folgt anfangen:

```python
name = input("Hallo, wie heißt du? ")

antwort = print("Hallo "+name+", schön dich kennen zu lernen.")

antwort =  input("Hast du bereits Erfahrung im Programmieren gemacht? ")

if antwort == "Ja":
    print("Dann habe ich es ja mit einem richtigen Experten zu tun!")
elif antwort == "Nein":
    print("Was ja noch nicht ist, kann ja noch werden")
else:
    print("Hmmm, deine Antwort konnte ich nicht vertehen. Aber ich habe noch weitere Fragen...")

#...
```



