from list import LinkedList

def teste_1():
    values = [160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503]
    list = LinkedList()
    for val in values:
        list.add(val)
    assert list.average() == 550.6
    assert round(list.standardDeviation(), 2) == 572.03

def teste_2():
    values = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
    list = LinkedList()
    for val in values:
        list.add(val)
    assert round(list.average(), 2) == 60.32
    assert round(list.standardDeviation(), 2) == 62.26