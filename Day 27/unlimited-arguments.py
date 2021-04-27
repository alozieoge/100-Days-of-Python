def add(*args):
    print(args[0])
    # print(args)
    # print(type(args))
    sum_n = 0
    for n in args:
        sum_n += n
    return sum_n


# print(add(1, 2, 3, 4, 5))
# print(add(3, 5, 6))

def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        # self.model = kw["model"]  # Returns an error if "model" is provided as a parameter but not used in class init method.
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

my_car2 = Car(make="Nissan")
print(my_car2.model)
