import time


def read_manufacturers(filename):
    with open(filename) as f:
        return f.read().splitlines()


def is_duplicate(needle, haystack):
    for manufacturer in haystack:
        if manufacturer == needle:
            return True

    return False


def find_duplicate_manufacturers(filename="manufacturers.txt"):
    manufacturers = read_manufacturers(filename)
    manufacturers = [man.lower() for man in manufacturers]

    duplicates = []
    while manufacturers:
        manufacturer = manufacturers.pop()
        if is_duplicate(manufacturer, manufacturers):
            duplicates.append(manufacturer)

    return duplicates


find_duplicate_manufacturers()
