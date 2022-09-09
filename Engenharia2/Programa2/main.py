import sys, csv

if len(sys.argv) != 2:
    print("Usage: python3 main.py <input_file>")
    exit(1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()
    lines = [line for line in lines if line.strip() != '']

total = len(lines)

completeSections = []

class Section:
    def __init__(self, name):
        self.name = name
        self.lines = 0
        self.childs = 0
        self.father = None

sectionsStarters = ['class', 'if', 'def', 'for', 'while', 'try', 'except', 'with']
sectionStack = []


currIdent = 0
prevIdent = 0
fatherSection = None

for i in range(total + 1):
    line = lines[i] if i < total else 'ENDING'
    for i in range(len(line)//4):
        if line[i*4:i*4+4] != '    ':
            currIdent = i
            break

    stacksToPop = prevIdent - currIdent
    if currIdent < prevIdent:
        for i in range(stacksToPop):
            sec = sectionStack.pop()
            fatherSection = sec.father
            completeSections.append(sec)

    prevIdent = currIdent

    if line.strip().split(' ')[0] in sectionsStarters:
        sec = Section(line)
        sectionStack.append(sec)
        if fatherSection is not None:
            fatherSection.childs += 1
        sec.father = fatherSection
        fatherSection = sec

    for section in sectionStack:
        section.lines += 1

DELIMITER = ';'
QUOTE = "'"

with open('out.csv','a+', encoding="utf-8", newline='') as f:
    writer = csv.writer(f, delimiter=DELIMITER, quotechar=QUOTE, quoting=csv.QUOTE_ALL)
  
    header = ['PROGRAMA','NOME DA PARTE','FILHOS','LINHAS', 'TOTAL']

    writer.writerow(header)

    for section in completeSections:
        writer.writerow([filename, section.name[:-1], section.childs, section.lines, total])

    writer.writerow([filename, 'TOTAL', '', '', total])