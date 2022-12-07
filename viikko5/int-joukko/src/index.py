import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko(kasvatuskoko = 4, kapasiteetti=2)

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.lisaa(5)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
