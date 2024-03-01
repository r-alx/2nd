def sos(start,end):
    while start <= end:
        if start % 2 == 0:
            print(start,"is even")
        else:
            print(start,"is odd")
        start = start + 1
sos(1,6832)