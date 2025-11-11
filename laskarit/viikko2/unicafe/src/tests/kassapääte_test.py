import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_uusi_kassa_rahamaara_ja_lounaiden_maarat_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateis_edullinen_riittava_maksu_kasvattaa_kassaa_ja_palauttaa_vaihtorahan(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassa.edulliset, 1)
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240 + 400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateis_edullinen_ei_riita_ei_muuta_kassaa_eika_laskureita(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateis_maukas_ei_riita_ei_muuta_kassaa_eika_laskureita(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(vaihtoraha, 399)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortti_edullinen_onnistuu_veloittaa_kortilta_ja_kasvattaa_laskuria(self):
        kortti = Maksukortti(300)
        ok = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertTrue(ok)
        self.assertEqual(kortti.saldo_euroina(), 0.60)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_maukas_onnistuu_veloittaa_kortilta_ja_kasvattaa_laskuria(self):
        kortti = Maksukortti(500)
        ok = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertTrue(ok)
        self.assertEqual(kortti.saldo_euroina(), 1.00)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_edullinen_epaonnistuu_ei_veloitusta_eika_laskuria(self):
        kortti = Maksukortti(200)
        ok = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(ok)
        self.assertEqual(kortti.saldo_euroina(), 2.00)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_maukas_epaonnistuu_ei_veloitusta_eika_laskuria(self):
        kortti = Maksukortti(399)
        ok = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(ok)
        self.assertEqual(kortti.saldo_euroina(), 3.99)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_lataa_positiivinen_summa_muuttaa_molempia(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo_euroina(), 5.00)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 500)

    def test_kortille_lataa_negatiivinen_ei_muuta_mitaan(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(kortti.saldo_euroina(), 10.00)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kassa_rahaa_euroina_toimii(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)