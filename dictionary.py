class Dictionary:
    def __init__(self):
       self.coppie={}

    def addWord(self,parola1:str,parola2:list):

      if len(parola2)==1:
          self.coppie[parola1]=parola2
      else:
          for s in parola2:
            s.lower()
            self.coppie[parola1.lower()]=parola2

    def translate(self,parola:str):
        return self.coppie[parola]


    def translateWordWildCard(self):
        pass