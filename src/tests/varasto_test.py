import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
         
    def test_negatiivinen_otto(self):
        saatu_maara = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_riittava_saldo(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(saatu_maara, 5)
        self.assertAlmostEqual(self.varasto.saldo, 5)    

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_tilavuus(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_lisays_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 5)

    def test_ottaminen_tasa_saldo(self):
        self.varasto.lisaa_varastoon(10)
        saatu_maara = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(saatu_maara, 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_varasto_tyhjennys(self):
        self.varasto.ota_varastosta(5)  # Varasto tyhjää
        self.assertAlmostEqual(self.varasto.saldo, 0)  # Ei pitäisi saada mitään

    def test_ottaminen_varasto_tayttaaminen(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)  # Varasto täynnä
        saatu_maara = self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(saatu_maara, 0)  # Ei pitäisi saada mitään

    def test_lisays_tayttaaminen_varasto(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Varasto täynnä
        self.varasto.lisaa_varastoon(5)  # Yritetään lisätä yli
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Saldo ei muutu
    def test_lisays_tayttaaminen_varasto(self):
        self.varasto.lisaa_varastoon(10)  # Täytetään varasto
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Varasto täynnä
        self.varasto.lisaa_varastoon(0)  # Yritetään lisätä 0
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Saldo ei muutu    
    def test_ottaminen_rajatapauksena(self):
        self.varasto.lisaa_varastoon(10)  # Täytetään varasto
        saatu_maara = self.varasto.ota_varastosta(10)  # Otetaan kaikki
        self.assertAlmostEqual(saatu_maara, 10)  # Pitäisi saada kaikki
        self.assertAlmostEqual(self.varasto.saldo, 0)  # Varasto tyhjentynyt
    def test_lisays_rajatapauksena(self):
        self.varasto.lisaa_varastoon(10)  # Täytetään varasto
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)  # Varasto täynnä
        self.varasto.lisaa_varastoon(1)  # Yritetään lisätä yli
        self.assertAlmostEqual(self.varasto.saldo, 10)  # Saldo ei muutu, koska varasto on täynnä
    def test_str_metodi(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(str(self.varasto), "saldo = 5.0, vielä tilaa 5.0")    

