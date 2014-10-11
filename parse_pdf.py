from subprocess import call
from sys import argv
import os

class StripContent:
    def __init__(self,pdf):
        self.pdf = pdf
        self.text = self.pdf.split(".")[0].split("/")[1]+".txt"
        self.root = self.pdf.split(".")[0].split("/")[1]
        self.doc = self.parseText()
    
    def parseText(self):
        #extract all the text    
        if not os.path.exists("textDocs"):
            os.mkdir("textDocs")    
        call(["pdftotext","-layout",self.pdf,"textDocs"+self.text])
        doc = []
        with open(self.text,"r") as f:
            for line in f:
                doc.append(line)
        return doc

    def parseImages(self):

        if not os.path.exists("images"):
            os.mkdir("images")
        if not os.path.exists("images/"+self.root):
            os.mkdir("images/"+self.root)

        print "parsing out images.."
        #extract all the images
        call(["pdfimages","-j",self.pdf,"images/"+self.root+"/"])

