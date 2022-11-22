list = [1,2,7,4,5]
def is_sorted(list):
    flag = 0
    counter = 1
    while counter < len(list):
        if list[counter] < list[counter -1]:
            flag = 1
        counter += 1

    if(not flag):
        print("Sorted")
    else:
        print("Not Sorted")

is_sorted(list)
