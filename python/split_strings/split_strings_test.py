from split_strings import solution

def test_example1():
    got = solution("abc")
    want = ["ab", "c_"]
    assert got == want

def test_example2():
    got = solution("abcdef")
    want = ["ab", "cd", "ef"]
    assert got == want
