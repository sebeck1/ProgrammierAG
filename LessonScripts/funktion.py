erfragte_namen = []

def zeigeNameaufKonsole(name):
    erfragte_namen.append(name)
    print("Hallo "+ name+ " schön, dass du dich dazu gesellst.")


erfragter_name = input("Wie heißt du?")

zeigeNameaufKonsole(erfragter_name)
