import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_oikea_alkutilanne(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 1000 * 100)

    def test_kateisosto_maksu_riittava_vaihtorahat(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_kateisosto_maksu_riittava_myydyt_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_maksu_ei_riittava_myydyt_ei_kasva(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)


    def test_kateisosto_maksu_ei_riittava_raha_ei_muutu(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 1000*100)
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 1000*100)

    def test_maksukortti_maksu_riittava_veloitus(self):
        k = Maksukortti(240 + 400)
        self.kassa.syo_maukkaasti_kortilla(k)
        self.assertEqual(str(k), "saldo: 2.4")
        self.kassa.syo_edullisesti_kortilla(k)
        self.assertEqual(str(k), "saldo: 0.0")

    def test_maksukortti_maksu_riittava_palautus(self):
        k = Maksukortti(240 + 400)
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(k))
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(k))

    def test_maksukortti_maksu_riittava_myydyt_kasvaa(self):
        k = Maksukortti(240 + 400)
        self.kassa.syo_edullisesti_kortilla(k)
        self.assertEqual(self.kassa.edulliset, 1)
        self.kassa.syo_maukkaasti_kortilla(k)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maksukortti_ei_tarpeeksi_rahaa_raha_ei_muutu(self):
        k = Maksukortti(10)
        self.kassa.syo_maukkaasti_kortilla(k)
        self.assertEqual(str(k), "saldo: 0.1")
        self.kassa.syo_edullisesti_kortilla(k)
        self.assertEqual(str(k), "saldo: 0.1")

    def test_maksukortti_ei_tarpeeksi_rahaa_myydyt_ei_muutu(self):
        k = Maksukortti(10)
        self.kassa.syo_edullisesti_kortilla(k)
        self.assertEqual(self.kassa.edulliset, 0)
        self.kassa.syo_maukkaasti_kortilla(k)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_maksukortti_ei_tarpeeksi_rahaa_palauttaa_false(self):
        k = Maksukortti(10)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(k))
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(k))

    def test_maksukortti_ostot_ei_muuta_kassan_rahaa(self):
        k = Maksukortti(240 + 400 + 10)
        self.kassa.syo_edullisesti_kortilla(k)
        self.kassa.syo_maukkaasti_kortilla(k)
        self.kassa.syo_edullisesti_kortilla(k)
        self.assertEqual(self.kassa.kassassa_rahaa, 1000 * 100)

    def test_maksukortin_lataus(self):
        k = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(k, 100)
        self.assertEqual(str(k), "saldo: 1.0")
        self.assertEqual(self.kassa.kassassa_rahaa, 1000 * 100 + 100)

    def test_makskukortin_lataus_negatiivinen(self):
        k = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(k, -10)
        self.assertEqual(str(k), "saldo: 0.0")
        self.assertEqual(self.kassa.kassassa_rahaa, 1000*100)
