from dictionary import Dictionary


class Translator:

    def __init__(self,dictionary:Dictionary):
        self.dictionary = Dictionary()

    def printMenu(self):
        print("1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Exit")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r',encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                (parola1,parola2) = line.split(' ')

                self.dictionary.addWord(parola1,[parola2])


    def handleAdd(self, parola1:str,parole:list):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dictionary.addWord(parola1, parole)
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        soluzione=""

        if self.dictionary.coppie[query]!=None:
            for el in self.dictionary.coppie[query]:
                soluzione+=el+"\t"
        else:
            soluzione+="nessuna parola trovata"
        return soluzione



        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass