# Hang Man

Bevor wir uns mit dem Programmieren des Spiels beschäftigen, müssen wir noch zwei weitere Konzepte lernen:
+ die [while-Schleife](#while-schleife)
+ die [Funktion](#die-funktion).

## while-Schleife
Die while-Schleife in Python dient dazu eine Anweisung so lange durchführen zu lassen, bis eine bestimmte Bedingung erfüllt ist. Die while-Schleife in Python hat dabei den folgenden Aufgbau:
```py
while Bedingung:
    Anweisung
```

So gibt der nachfolgende Code 
```py
while i<5:
    print(i)
    i+=1
```
die Zahlen von 1 bis 4 aus. Hätte man gerne noch die 5 mit dabei so müssste der Code umgeschrieben werden zu
```py
while i<=5:
    print(i)
    i+=1
```
oder
```py
while i<6:
    print(i)
    i+=1
```
## Aufgabe
>Schreibe eine while-Schleife, die Zahlen von 0 bis 100 ausgeben und auf der Konsole anzeigen.


Aber **Achtung**: Bei der Programmierung von Schleifen passiert es leicht, das diese endlos laufen. Das könnte beispielsweise im obigen Code dann passieren, wenn i mit i+=1 nicht um eins erhöht werden würde. Sollte dies doch passieren und das Programm unendlich die Anweisung ausführen, so lässt sich das Programm mittels der Tastenkombination STRG + C abbrechen.

## Die Funktion in Python
In Python gibt es eine ganze Reihe unterschiedlicher Funktionen. So gibt es anonyme, Lambda-Funktionen, Rekursive Funktionen etc. die in Python benutzt werden, um zum einen uns das Leben ein wenig einfacher zu machen und Schreibarbeit zu ersparren, aber auch, um den Code übersichtlicher zu gestalten. Erinnerst du dich beispielsweise noch an die Funktion 
```py
random.choice(list)
```
aus dem vorherigen Passwortgenerator zurück? Hier war das Anhängsel *.choice* ebenfalls eine Funktion. Wir wollen jedoch heute eigene Funktion kreieren.
Die Definition eigener Funktionen beginnt mit dem Schlüsselwort *def*. Dem folgt der Funktionsname, für den dieselben Regeln wie für Variablenamen gelten (bspw. immer klein schreiben, müssen zusammenhängend geschrieben sein...). Mit Parametern übergeben wir dann die Daten an die Funktion. Parameter müssen in die runden Klammern gestellt werden:
```py
def funktionsname(para1, para2, para3):
    code
    mehr code
    noch mehr code
    
```
Folgende <span style="color:#FFCCCB">Regeln </span>  sind bei der Programmierung und Anwendung von Funktionen jedoch zu beachten:
+ Funktionen müssen definiert werden, bevor sie verwendet werden können. Deswegen ist es üblich, zuerst alle Funktionen zu definieren und erst im Anschluss daran den restlichen Code anzugeben.
+ Funktionen ohne Parameter sind zulässtig, die runden Klammenr müssen jedoch immer mit angegeben werden
+ Funktionen können vorzeitig mit dem Wort <span style="color:rgb(135,206,235)">return </span> verlassen werden, Die Verwendung von <span style="color:rgb(135,206,235)">return </span> ist jedoch optional.
+ Mit dem Wort <span style="color:rgb(135,206,235)">return </span> kann die Funktion ein Ergebnis zurückgeben. Hierfür ist jeder Python-Datentyp erlaubt, also auch Listen etc. Auf diese Weise kann eine Funktion ganz einfach mehrere Werte zurückgeben.

## Aufgabe
>Schreibe eine Funktion, die über den Parameter einen Namen entgegennimmt und diesen dann auf der Konsole ausdruckt.

## Nun sind wir bereit
Nun können wir uns mit dem Programmierung von Hang-Man beschäftigen. [Hier gehts weiter](./hang_man.md)