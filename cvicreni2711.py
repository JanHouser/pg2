class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.email = email
        self.telefon = telefon

    def __str__(self):
        return f'Osoba({self.jmeno}, {self.email}, {self.telefon})'
    
    @property
    def jmeno(self):
        return self.__jmeno
    
    @jmeno.setter
    def jmeno(self, hodnota:str):
        for c in hodnota:
            if not c.isalpha() and not c.isspace():
                raise InvalidData(f'CHYBNE ZADANE JMENO "hodnota"')
        self.__jmeno = hodnota



    @property
    def telefon(self):
        return self.__telefon
    
    @telefon.setter
    def telefon(self, hodnota: str):
        for c in hodnota:
            if not len(hodnota) == 13:
                raise InvalidData(f'Cislo msi obsahovat 13 znaku')
            if hodnota[0] != '+'

if __name__ == "__main__":


    o1 = Osoba("Tomas", "+42077888999", "ahoj@email.cz")
    print(o1)

    o1.jmeno = 'Jan Novák'
    print(o1)
     