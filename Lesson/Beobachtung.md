# Beobachtung

Herzlichen Glückwunsch, du hast soeben dein erstes Programm ausgeführt!

Was bei der Ausführung passiert? Du hast der _Funktion_ (ja, die gibt es nicht nur in der Mathematik) einen sogenannten _Paramerer_ übergeben. Genauer handelt es sich bei dem Parameter um einen _String_. An dieser Stelle wollen wir uns nicht mit Datentypen befassen. Falls du  jedoch mehr darüber erfahren möchtest, kannst du dies über diese Seite tun: https://www.sivakids.de/python-datentypen/#:~:text=Python%20Datentypen%20sind%20somit%20die,Variablen%2C%20Listen%20oder%20Tupel%20sein.

## Aufgabe 
1) Versuche mehrere print-Befehle auf einmal in der IDLE auszuführen. Was fällt dir auf?

=> [Wie führe ich ein Programm aus?](../Themen/Einrichtung/Wie%20f%C3%BChre%20ich%20ein%20Programm%20aus.md)

## Mit Variablen arbeiten
Wie wir gelernt haben, können wir mit dem print-Befehl etwas auf die Konsole ausgeben:
```python
print("Hallo Max")
# Die Ausgabe ist "Hallo Max"
```
Wir können aber auch "Max" als _Variable_ abspeichern. Man kann sich die Variable quasi als eine Art Schubladenkasten vorstellen, in dem etwas, hier in dem Fall der Name Max, abgeleckt wird. Das sieht dann wie folgt aus:
```python
name = "Max"

print("Hallo " + name)
```
### ZwiscchenAufgabe
1) Mache dir Gedanken darüber, was der Vorteil von Variablen sein könnte.

Der Vorteil einer solchen Variable ist, dass wir nicht nur "Max" sondern alle möglichen Werte in dieser Variable ablegen können. Dies zeigt das folgende Beispiel:

```python
name = input("Wie heißt du? ")

print("Hallo " + name)

```

Durch den input-Befehl erhält die Variable _name_ nun einen neuen Wert, der dann durch den print-Befehl ausgegeben wird.

## Aufgabe
1) Denke dir selber ein paar Beispiele aus.
      
2) Schreibe einen kleinen Dialog zwischen Computer und Mensch, indem der Computer dir verschiedene Fragen stellt, die du beantwortest.
