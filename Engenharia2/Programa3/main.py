from list import LinkedList

def test_case_1():
    testClass = LinkedList()
    testClass.add(130, 186)
    testClass.add(650, 699)
    testClass.add(99, 132)
    testClass.add(150, 272)
    testClass.add(128, 291)
    testClass.add(302, 331)
    testClass.add(95, 199)
    testClass.add(945, 1890)
    testClass.add(368, 788)
    testClass.add(961, 1601)
    b0, b1 = testClass.linearRegression()
    r, rr = testClass.correlation()
    assert format(b0, '.2f') == '-22.55'
    assert format(b1, '.4f') == '1.7279'
    assert format(r, '.4f') == '0.9545'
    assert format(rr, '.4f') == '0.9111'
    assert format(testClass.estimate(386), '.3f') == '644.429'
    assert testClass.size == 10

def test_case_2():
    testClass = LinkedList()
    testClass.add(130, 15)
    testClass.add(650, 69.9)
    testClass.add(99, 6.5)
    testClass.add(150, 22.4)
    testClass.add(128, 28.4)
    testClass.add(302, 65.9)
    testClass.add(95, 19.4)
    testClass.add(945, 198.7)
    testClass.add(368, 38.8)
    testClass.add(961, 138.2)
    b0, b1 = testClass.linearRegression()
    r, rr = testClass.correlation()
    assert format(b0, '.3f') == '-4.039'
    assert format(b1, '.4f') == '0.1681'
    assert format(r, '.4f') == '0.9333'
    assert format(rr, '.4f') == '0.8711'
    assert format(testClass.estimate(386), '.3f') == '60.858'
    assert testClass.size == 10

def test_case_3():
    testClass = LinkedList()
    testClass.add(163, 186)
    testClass.add(765, 699)
    testClass.add(141, 132)
    testClass.add(166, 272)
    testClass.add(137, 291)
    testClass.add(355, 331)
    testClass.add(136, 199)
    testClass.add(1206, 1890)
    testClass.add(433, 788)
    testClass.add(1130, 1601)
    b0, b1 = testClass.linearRegression()
    r, rr = testClass.correlation()
    print(b0, b1, r)
    assert format(b0, '.2f') == '-23.92'
    assert format(b1, '.5f') == '1.43097'
    assert format(r, '.4f') == '0.9631'
    assert format(rr, '.4f') == '0.9276'
    assert format(testClass.estimate(386), '.4f') == '528.4294'
    assert testClass.size == 10

def test_case_4():
    testClass = LinkedList()
    testClass.add(163, 15)
    testClass.add(765, 69.9)
    testClass.add(141, 6.5)
    testClass.add(166, 22.4)
    testClass.add(137, 28.4)
    testClass.add(355, 65.9)
    testClass.add(136, 19.4)
    testClass.add(1206, 198.7)
    testClass.add(433, 38.8)
    testClass.add(1130, 138.2)
    b0, b1 = testClass.linearRegression()
    r, rr = testClass.correlation()
    assert format(b0, '.3f') == '-4.604'
    assert format(b1, '.6f') == '0.140164'
    assert format(r, '.4f') == '0.9480'
    assert format(rr, '.4f') == '0.8988'
    assert format(testClass.estimate(386), '.4f') == '49.4994'