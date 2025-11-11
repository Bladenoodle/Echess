import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataus_kasvattaa_saldoa(self):
        self.kortti.lataa_rahaa(250)
        self.assertEqual(self.kortti.saldo_euroina(), 12.5)

    def test_otto_vahentaa_kun_rahaa_tarpeeksi(self):
        ok = self.kortti.ota_rahaa(400)
        self.assertTrue(ok)
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_otto_ei_onnistu_kun_rahaa_ei_tarpeeksi(self):
        ok = self.kortti.ota_rahaa(2000)
        self.assertFalse(ok)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)
