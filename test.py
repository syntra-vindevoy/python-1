# def test():
#     age = int(input("number: "))
#     if age < 5:
#         print("hello")
#     elif age == 5:
#         print("nice")
#     else:
#         print("go home")
#
#
# test()

# a = 1
#
# def toto():
#     global a
#     a = 2
#     print (a)
#
# toto()
# print(a)


#test module

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

if __name__ == "mane":
    def test1_int():
        for i in range(-5, 0):
            assert absolute_value(i) == -i, f"Value: {i}"  # format naar string
        for i in range(0, 6):
            assert absolute_value(i) == i, f"Value: {i}"

    def test_float():
        assert absolute_value(2.5)  == 2.5

    def test_string():
        ok = True

        try:
            assert absolute_value("a")

        except:
            ok = False

            assert not ok, "Does not work as expected"


    test1_int()
    test_float()
    test_string()


