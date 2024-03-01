#create a function from 1 to 50 to check that is even or odd
def function(num):
    counter = 1
    while counter <= num:        
        if counter % 2 == 0:
            print(counter,"is even")
        else:
            print(counter,"is odd")
        counter = counter + 1
function(100)
