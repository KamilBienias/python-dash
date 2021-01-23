# Etap7. Odcinek: Dekoratory w Pythonie

def dekorator(func):
    print("Python")
    return func


def hello_world():
    print("Hello World")


hello_world_dekorator = dekorator(hello_world)
print(type(hello_world_dekorator))

print("Uruchomienie funkcji hello_world_decorator()")
hello_world_dekorator()

@dekorator
def hello_world_2():
    print("hello world")

print()
print("Uruchomienie funkcji hello_world_2() z adnotacja")
hello_world_2()

