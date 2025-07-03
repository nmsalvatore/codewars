from counting import duplicate_count

def test_case1():
    got = duplicate_count("")
    want = 0
    assert got == want

def test_case2():
    got = duplicate_count("abcde")
    want = 0
    assert got == want

def test_case3():
    got = duplicate_count("abcdeaa")
    want = 1
    assert got == want

def test_case4():
    got = duplicate_count("abcdeaB")
    want = 2
    assert got == want

def test_case5():
    got = duplicate_count("Indivisibilities")
    want = 2
    assert got == want
