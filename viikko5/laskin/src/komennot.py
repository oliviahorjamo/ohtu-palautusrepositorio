
class Operaatio:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.lue_syote = lue_syote
        self.sovelluslogiikka = sovelluslogiikka
        self.luku = 0
        self.viim_luku = 0

    def suorita(self):
        self.luku = self.lue_syote()
        self.laske()

    def laske(self):
        return 0

    def kumoa(self):
        return 0

class Summa(Operaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def laske(self):
        self.viim_luku = int(self.luku)
        return self.sovelluslogiikka.plus(int(self.luku))

    def kumoa(self):
        return self.sovelluslogiikka.miinus(self.viim_luku)


class Erotus(Operaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def laske(self):
        return self.sovelluslogiikka.miinus(int(self.luku))


class Nollaus(Operaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def laske(self):
        return self.sovelluslogiikka.nollaa()


class Kumoa(Operaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def laske(self):
        pass
        #return self.sovelluslogiikka.aseta_arvo(self.viim_luku)

