import pandas as pd
from unidecode import unidecode
class ToCSV:
    def __init__(self,words,tables=False,graphics=False):
        self.words = [word.lower() for word in words] #list of words to look for in pdf
        self.tables = tables
        self.graphics = graphics

    def to_csv(self,doc):
        csv = "out.csv"
        df = pd.DataFrame(columns=self.words)
        for line in doc:
            line = unidecode(line)
            sentence = line.split(" ")
            sentence = [word.lower() for word in sentence]
            test = [word for word in sentence if word in self.words]
            if test != []:
                
                    
