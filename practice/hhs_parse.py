from subprocess import call
from sys import argv
from unidecode import unidecode
#call(["pdftotext","-layout",argv[1]])

pdf = argv[1].split(".")[0]+".txt"
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

for entity in possible_links:
    start = entity[0]
    
    start = start.split(" ")
    start = [elem for elem in start if "http" in elem][0]
    to_add = []
    pdf_file = False
    
    for sentence in entity[1:]:
        sentence = sentence.split(" ")
        counter = 0
        for word in sentence:
            if ("/" in word or "%" in word or "&" in word) and not("http" in word):
                to_add.append(word)
                counter += 1
                if ".pdf" in word: 
                    stop = counter
                    pdf_file = True

    url = start
    if pdf_file:
        for i in to_add[:stop]:
            url += i
    else:
        for i in to_add:
            url += i
    print url
