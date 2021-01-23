# Etap7. Odcinek: Dekoratory w Pythonie

from datetime import datetime

print("Aktualny czas")
print(datetime.now())

print()
print("Tylko godzina")
print(datetime.now().hour)


def dekorator(func):
    def wrapper():
        # bedzie uruchamial nasza funkcje w tych godzinach
        if 9 <= datetime.now().hour <= 17:
            func()
        # poza godzinami roboczymi nic nie robi
        else:
            pass
    return wrapper


print()


# bez adnotacji dekoratora funckja pora_dnia bedzie zawsze wywolywana
@dekorator
def pora_dnia():
    print("Wywolanie pora_dnia")
    print("Godziny robocze")

pora_dnia()

# mozna innym sposobem, ale z adnotacja lepiej
# pora_dnia = dekorator(pora_dnia)