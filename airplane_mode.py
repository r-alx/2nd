fruit = []
def my_fruits_store():
    for f in range(5):
        fruitss = input("Enter fruit Name that you have in your store:)")
        fruit.append(fruitss.lower())
my_fruits_store()

print("Store Board-- Fruits in our store:",fruit)
 
your_choice=input("Ënter your choice")
if your_choice.lower()  in fruit:
    print("pay the price  and pick your fruits")
else:
    print("outa of my shop!!!QUICK!!!")

print(fruit)