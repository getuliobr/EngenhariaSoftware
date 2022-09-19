from list import LinkedList


N = int(input('Dados: '))

ll = LinkedList()

for i in range(N):
    x, y = map(float, input("X Y separado por espaco: ").split(' '))
    ll.add(x, y)

b0, b1 = ll.linearRegression()
r, rr = ll.correlation()

print('b0 = {:.2f}'.format(b0))
print('b1 = {:.4f}'.format(b1))
print('r = {:.4f}'.format(r))
print('r^2 = {:.4f}'.format(rr))

x = float(input('Estimar: '))
print('y = {:.3f}'.format(ll.estimate(x)))