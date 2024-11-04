class Varasto:
    def __init__(self, tilavuus: float, alku_saldo: float = 0.0) -> None:
        """Alustaa varaston annetulla kapasiteetilla ja alkusaldoilla."""
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            raise ValueError("Tilavuus tulee olla suurempi kuin 0.")

        if alku_saldo < 0.0:
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            self.saldo = alku_saldo
        else:
            self.saldo = tilavuus  # Asetetaan saldo täyteen kapasiteettiin

    def paljonko_mahtuu(self) -> float:
        """Laskee, kuinka paljon lisää mahtuu varastoon."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara: float) -> None:
        """Lisää tietty määrä tavaraa varastoon."""
        if maara < 0:
            raise ValueError("Lisättävän määrän tulee olla ei-negatiivinen.")
        if maara <= self.paljonko_mahtuu():
            self.saldo += maara
        else:
            raise ValueError("Ei voida lisätä, varasto täyttyisi liikaa")

    def ota_varastosta(self, maara: float) -> float:
        """Ottaa tietyn määrän tavaraa varastosta, palauttaen todellisen otetun määrän."""
        if maara < 0:
            raise ValueError("Otettavan määrän tulee olla ei-negatiivinen.")
        if maara > self.saldo:
            # Jos yritetään ottaa enemmän kuin on saatavilla
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan  # Palautetaan se, mitä voidaan ottaa

        self.saldo -= maara
        return maara

    def __str__(self) -> str:
        """Palauttaa merkkijonon, joka kuvaa varaston tilaa."""
        return f"saldo = {self.saldo}, vielä tilaa = {self.paljonko_mahtuu()}"

# Esimerkki Varasto-luokan käytöstä
varasto = Varasto(100, 50)
print(varasto)  # saldo = 50, vielä tilaa = 50
try:
    varasto.lisaa_varastoon(60)  # Yritetään lisätä liikaa
except ValueError as e:
    print(e)  # Tulostaa virheilmoituksen

varasto.lisaa_varastoon(30)  # Lisätään 30
print(varasto)  # saldo = 80, vielä tilaa = 20

removed = varasto.ota_varastosta(90)  # Yritetään ottaa liikaa
print(f"Otettiin varastosta: {removed}")  # Otetaan vain 80, mikä on maksimimäärä
print(varasto)  # saldo = 0, vielä tilaa = 100
    
