import translator as tr
import dictionary as d
t = tr.Translator(d)


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Inserisci numero:")

    # Add input control here!

    if int(txtIn) == 1:
        print("1. Aggiungi nuova parola")

        testo= input("OK, quale parola vuoi aggiungere? ")
        parole=testo.split(" ")
        if len(parole)<2:
            print("non trovato")

        parola=parole[0]
        traduzioni=parole[1:]
        t.handleAdd(parola,traduzioni)
        for (k,list) in t.dictionary.coppie.items():
            print(f"{k}: {', '.join(list)}")


    if int(txtIn) == 2:
        print("2. Cerca una traduzione")
        testo = input("OK, quale parola vuoi cercare? ")
        print(t.handleTranslate(testo.lower()))

        pass
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        False
        break