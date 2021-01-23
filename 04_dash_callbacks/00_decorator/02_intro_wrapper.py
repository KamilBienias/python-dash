# Etap7. Odcinek: Dekoratory w Pythonie

def dekorator(func):
    def wrapper():
        func()
        print("Wywolanie funkcji wrapper")
    return wrapper

@dekorator
def func_2():
    print("Wywolanie func_2")

func_2()
