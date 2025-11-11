import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        k = Maksukortti(200)
        k.syo_edullisesti()
        self.assertEqual(k.saldo_euroina(), 2.0)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        k = Maksukortti(300)
        k.syo_maukkaasti()
        self.assertEqual(k.saldo_euroina(), 3.0)

    def test_negatiivisen_summan_lataus_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-100)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)

    def test_voin_ostaa_edullisen_kun_saldo_tasan_edullinen(self):
        k = Maksukortti(250)
        k.syo_edullisesti()
        self.assertEqual(k.saldo_euroina(), 0.0)

    def test_voin_ostaa_maukkaan_kun_saldo_tasan_maukas(self):
        k = Maksukortti(400)
        k.syo_maukkaasti()
        self.assertEqual(k.saldo_euroina(), 0.0)

    def test_saldon_maksimi_150_euroa(self):
        self.kortti.lataa_rahaa(999999)
        self.assertEqual(self.kortti.saldo_euroina(), 150.0)
