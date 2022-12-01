import string


def smallest_biggest(a: str):
    letters = string.ascii_letters  #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    kleinste = 51
    grootste = 0
    kleinste_opl = None
    grootste_opl = None
    for i in a:
        if i in letters:
            if letters.index(i) < kleinste:
                kleinste = letters.index(i)
                kleinste_opl = letters[kleinste]
            if letters.index(i) > grootste:
                grootste = letters.index(i)
                grootste_opl = letters[grootste]

    #print(kleinste_opl, grootste_opl)
    opl = (kleinste_opl, grootste_opl)
    #print(opl)
    return opl


if __name__ == "__main__":
    smallest_biggest("abCd  uidhczei UIOH*")
    assert smallest_biggest("  *") == (None, None)

