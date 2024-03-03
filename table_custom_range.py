#write a function that can get number of the table, start and end, write the table of given number from start to end of the given.

def func(num, start, end):

    while start <= end:
        print(num,"*",start,"=",num* start)
        start = start + 1
table = int(input("the table of 5"))
func(table,6,10)