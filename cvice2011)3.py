class ChybnaCastka(Exception):
    pass


class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def vloz(self, suma):
        if suma <= 0:
            raise ChybnaCastka("Nelze pridat nulovou nebo zapornou castku")
        self.__zustatek += suma

    def vyber(self, suma):
        if suma <= 0:
         raise ChybnaCastka("Nelze pridat nulobou nebo zapornou castku")
        if suma > self.__zustatek:
         
    

    def __str__(self):
        return f'Ucet vlastni {self.jmeno} a je na nem {self.__zustatek} kc'


if __name__ == "__main__":
    try:
     neni hotovo dodelat