from abc import ABC, abstractmethod

class Uzytkownik(ABC):
    _licznik = 0

    def __init__(self, nazwa: str, email: str):
        self.nazwa = nazwa
        self.email = email
        self._aktywny = True
        Uzytkownik._licznik += 1
        self._id = f"{self._prefiks}-{Uzytkownik._licznik:03d}"

    @property
    @abstractmethod
    def _prefiks(self) -> str:
        ...

    @property
    def id(self):
        return self._id

    @property
    def aktywny(self):
        return self._aktywny

    @property
    def email(self):
        return self._email

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, wartosc: str):
        if not isinstance(wartosc, str):
            raise TypeError("Nazwa musi być tekstem.")
        wartosc = wartosc.strip()
        if len(wartosc) < 3:
            raise ValueError("Nazwa musi mieć conajmniej 3 litery.")
        self._nazwa = wartosc

    @email.setter
    def email(self, wartosc: str):
        if not isinstance(wartosc, str):
            raise TypeError("Email musi być tekstem.")
        wartosc = wartosc.strip()
        if wartosc.count("@") != 1:
            raise ValueError("Email musi zawierać dokładnie 1 znak @.")
        miejsce = wartosc.find("@")
        if miejsce == 0 or miejsce == len(wartosc) - 1:
            raise ValueError("Email nie może zaczynać się lub kończyć znakiem @.")
        if "." not in wartosc[miejsce + 1:]:
            raise ValueError("Po znaku @ musi występować kropka.")
        _, domena = wartosc.split("@")
        if domena.startswith(".") or domena.endswith("."):
            raise ValueError("Domena emailu nie może zaczynać się lub kończyć kropką.")
        if " " in wartosc:
            raise ValueError("Spacja nie może występować w emailu.")
        self._email = wartosc




