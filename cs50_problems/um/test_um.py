from um import count

def test_independent_um():
    assert count("um UM, Um, um") == 4
    assert count("UM UM mu sds um") == 3

def test_inside_word_um():
    assert count("umsds UMSDS um UM sdum") == 2
    assert count("umsasdumum UMUM um UM") == 2

def test_all():
    assert count("umsUM, um, Umsd, U,m UM") == 2
    assert count("umsdsd umUM") == 0
