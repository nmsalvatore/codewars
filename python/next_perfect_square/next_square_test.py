from next_square import find_next_square

def test_example1():
    got = find_next_square(121)
    want = 144
    assert got == want

def test_example2():
    got = find_next_square(625)
    want = 676
    assert got == want

def test_example3():
    got = find_next_square(114)
    want = -1
    assert got == want
