from list import LinkedList


N = int(input('Qtde de dados: '))

listaTamanhos = LinkedList()
mediaTamanhos = LinkedList()

for i in range(N):
    inputs = list(map(float, input("LOC Metodos/Paginas(separado por espaco): ").split(' ')))
    if(len(inputs) == 1):
        listaTamanhos.add(inputs[0])
    else:
        listaTamanhos.add(inputs[0]/inputs[1])

PP, P, M, G, GG = listaTamanhos.estimateRange()
print('PP:', PP)
print('P:', P)
print('M:', M)
print('G:', G)
print('GG:', GG)
