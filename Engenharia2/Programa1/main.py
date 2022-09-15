from list import LinkedList

data = input('Dados: ')
data = data.split(' ')
list = LinkedList()
for val in data:
  list.add(float(val))

print(list.average(), list.standardDeviation())

#Casos de teste
#160 591 114 229 230 270 128 1657 624 1503
#15.0 69.9 6.5 22.4 28.4 65.9 19.4 198.7 38.8 138.2
#186 699 132 272 291 331 199 1890 788 1601