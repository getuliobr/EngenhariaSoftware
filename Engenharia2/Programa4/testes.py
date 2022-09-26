from list import LinkedList

def test_case_1():
    l = LinkedList()
    l.add(18/3)
    l.add(18/3)
    l.add(25/3)
    l.add(31/3)
    l.add(37/3)
    l.add(82/5)
    l.add(82/4)
    l.add(87/4)
    l.add(89/4)
    l.add(230/10)
    l.add(85/3)
    l.add(87/3)
    l.add(558/10)

    PP, P, M, G, GG = l.estimateRange()
    LPP, LP, LM, LG, LGG = l.estimateLimits()
    
    assert l.size == 13
    assert l.averageLog() - 2.8015 < 0.0001
    assert l.logVariants() - 0.4363 < 0.0001
    assert l.logStandardDeviation() - 0.6605 < 0.0001
    assert PP - 1.4805 < 0.0001
    assert P - 2.141 < 0.001
    assert M - 2.8015 < 0.0001
    assert G - 3.462 < 0.001

    assert LPP - 4.3953 < 0.0001
    assert LP - 8.5081 < 0.0001
    assert LM - 16.4696 < 0.0001
    assert LG - 31.8811 < 0.0001
    assert LGG - 61.7137 < 0.0001

def test_case_2():
    l = LinkedList()

    l.add(7)
    l.add(12)
    l.add(10)
    l.add(12)
    l.add(10)
    l.add(12)
    l.add(12)
    l.add(12)
    l.add(12)
    l.add(8)
    l.add(8)
    l.add(8)
    l.add(20)
    l.add(14)
    l.add(18)
    l.add(12)

    PP, P, M, G, GG = l.estimateLimits()
    assert PP - 6.3375 < 0.0001
    assert P - 8.4393 < 0.0001
    assert M - 11.2381 < 0.0001
    assert G - 15.9650 < 0.0001
    assert GG - 19.9280 < 0.0001