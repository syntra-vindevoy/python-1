a = [1,2,3,4]
#def nested_sum(a):
 #   sum_of_a = sum(a)
  #  print(sum_of_a)
# nested_sum(a)

def nested_sum_other_method(a):
    total = 0
    for i in a:
        total = total + i
    print(total)
nested_sum_other_method(a)

print("kenji")



def nested_sum_other_method_(a) -> list[int]:
    _result = []
    for i, item in enumerate(a):
        _sum = sum(a[:i + 1])
        _result.append(_sum)

    return _result

a = nested_sum_other_method_(a)

print(a)