# A function named hello()
def hello():
    print("Hello, User")

hello()

#A function named pack
def pack(a, b, c):
    return [a, b, c]

print(pack(1, 2, 3))
print(pack("a", "b", "c"))

#A function called eat_lunch
def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + lunch_items[0])
    for i in range(1, len(lunch_items)):
        print("Next I eat " + lunch_items[i])

eat_lunch(["sandwich", "apple", "chips"])
eat_lunch([])