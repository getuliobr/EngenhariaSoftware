from list import LinkedList

def test_case_1():
    ll = LinkedList()
    ll.add(130, 186)
    ll.add(650, 699)
    ll.add(99, 132)
    ll.add(150, 272)
    ll.add(128, 291)
    ll.add(302, 331)
    ll.add(95, 199)
    ll.add(945, 1890)
    ll.add(368, 788)
    ll.add(961, 1601)
    b0, b1 = ll.linearRegression()
    r, rr = ll.correlation()
    assert b0 - -22.55 < 0.01
    assert b1 - 1.7279 < 0.0001
    assert r - 0.9545 < 0.0001
    assert rr - 0.9111 < 0.0001
    assert ll.estimate(386) - 644.429 < 0.001
    assert ll.size == 10

def test_case_2():
    ll = LinkedList()
    ll.add(130, 15)
    ll.add(650, 69.9)
    ll.add(99, 6.5)
    ll.add(150, 22.4)
    ll.add(128, 28.4)
    ll.add(302, 65.9)
    ll.add(95, 19.4)
    ll.add(945, 198.7)
    ll.add(368, 38.8)
    ll.add(961, 138.2)
    b0, b1 = ll.linearRegression()
    r, rr = ll.correlation()
    assert b0 - -4.039 < 0.001
    assert b1 - 0.1681 < 0.0001
    assert r - 0.9333 < 0.0001
    assert rr - 0.8711 < 0.0001
    assert ll.estimate(386) - 60.858 < 0.001
    assert ll.size == 10

def test_case_3():
    ll = LinkedList()
    ll.add(163, 186)
    ll.add(765, 699)
    ll.add(141, 132)
    ll.add(166, 272)
    ll.add(137, 291)
    ll.add(355, 331)
    ll.add(136, 199)
    ll.add(1206, 1890)
    ll.add(433, 788)
    ll.add(1130, 1601)
    b0, b1 = ll.linearRegression()
    r, rr = ll.correlation()
    print(b0, b1, r)
    assert b0 - -23.92 < 0.01
    assert b1 - 1.43097 < 0.00001
    assert r - 0.9631 < 0.0001
    assert rr - 0.9276 < 0.0001
    assert ll.estimate(386) - 528.4294 < 0.0001
    assert ll.size == 10

def test_case_4():
    ll = LinkedList()
    ll.add(163, 15)
    ll.add(765, 69.9)
    ll.add(141, 6.5)
    ll.add(166, 22.4)
    ll.add(137, 28.4)
    ll.add(355, 65.9)
    ll.add(136, 19.4)
    ll.add(1206, 198.7)
    ll.add(433, 38.8)
    ll.add(1130, 138.2)
    b0, b1 = ll.linearRegression()
    r, rr = ll.correlation()
    assert b0 - -4.604 < 0.001
    assert b1 - 0.140164 < 0.000001
    assert r - 0.9480 < 0.0001
    assert rr - 0.8988 < 0.0001
    assert ll.estimate(386) - 49.4994 < 0.0001