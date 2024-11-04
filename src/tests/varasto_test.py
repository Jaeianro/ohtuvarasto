import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    
    def setUp(self):
        self.varasto = Varasto(10)
    
    
    def test_lisays_yli_tilavuuden_heittaa_virheen(self):
        varasto_isolla_saldolla = Varasto(100, 50)
        with self.assertRaises(ValueError) as context:
            varasto_isolla_saldolla.lisaa_varastoon(60)  # Lisääminen 60 ylittää tilavuuden
        self.assertEqual(str(context.exception), "Ei voida lisätä, varasto täyttyisi liikaa")    
        
    
    def test_alkusaldo_negatiivinen(self):
        # Negatiivinen saldo asetetaan nollaksi
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0.0)    
    def test_alkusaldo_mahtuu_tilavuuteen(self):
        # Positiivinen saldo, joka mahtuu tilavuuteen, asetetaan sellaisenaan
        varasto = Varasto(10, 5)
        self.assertAlmostEqual(varasto.saldo, 5.0)
    def test_alkusaldo_ylittaa_tilavuuden(self):
        # Saldo, joka ylittää tilavuuden, asetetaan täyteen kapasiteettiin
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10.0)        

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0) 
    
         

    def test_konstruktori_luo_negatiivisen_tilavuuden_varaston(self):
        with self.assertRaises(ValueError):  # Oletetaan, että Varasto nostaa ValueError negatiivisesta kapasiteetista
            Varasto(-10)  # Yritetään luoda varasto negatiivisella tilavuudella      
            
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
    def test_ottaminen_negatiivinen(self):
        with self.assertRaises(ValueError):  # Oletetaan, että Varasto nostaa ValueError negatiivisista määristä
            self.varasto.ota_varastosta(-5)

    def test_lisays_negatiivinen(self):
        with self.assertRaises(ValueError):  # Oletetaan, että Varasto nostaa ValueError negatiivisista määristä
            self.varasto.lisaa_varastoon(-5)    
            

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_lisays_yli_varaston_tilavuuden(self):
        with self.assertRaises(ValueError) as context:
            self.varasto.lisaa_varastoon(15)  # Lisääminen 15 ylittää tilavuuden
        self.assertEqual(str(context.exception), "Ei voida lisätä, varasto täyttyisi liikaa") 
          
    
    def test_ottaminen_yli_varaston_saldon(self):
        self.varasto.lisaa_varastoon(5)  # Lisätään 5 tavaraa varastoon
        saatu_maara = self.varasto.ota_varastosta(10)  # Yritetään ottaa 10 tavaraa
        self.assertAlmostEqual(saatu_maara, 5)  # Pitäisi palauttaa vain 5, mikä oli saatavilla
        self.assertAlmostEqual(self.varasto.saldo, 0)  # Saldo pitäisi olla nolla, kun kaikki on otettu

   
            