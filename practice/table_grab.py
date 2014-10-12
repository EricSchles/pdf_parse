from subprocess import call
from sys import argv
from unidecode import unidecode
call(["pdftotext","-layout",argv[1]])

pdf = argv[1].split(".")[0]+".txt" #adjust this
doc = []
with open(pdf,"r") as f:
    for line in f:
        line = line.replace("\n","")
        line = unidecode(line)
        line = line.replace("\x0c","")
        if line != '':
            doc.append(line)

links = []
possible_links = []

for ind,line in enumerate(doc):
    open_ball = []
    if "http" in line:
        open_ball.append(line)
        open_ball.append(doc[ind+1])
        open_ball.append(doc[ind+2])
        open_ball.append(doc[ind+3])
        possible_links.append(open_ball)
