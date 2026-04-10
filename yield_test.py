def finite_sequence():
    num = 0
    while num < 1:
        print("=========="+str(num)+"============")
        yield num
        num += 1
        print("=========="+str(num)+"============")


for i in finite_sequence():
    print("asdfasdfa")