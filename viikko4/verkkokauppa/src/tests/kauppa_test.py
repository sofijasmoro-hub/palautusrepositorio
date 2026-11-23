import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            if tuote_id == 3:
                return Tuote(3, "juusto", 7)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_yksi_tuote_tilisiirto_oikeilla_tiedoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kaksi_eri_tuotetta_tilisiirto_oikeilla_tiedoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_kaksi_samaa_tuotetta_tilisiirto_oikeilla_tiedoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_tuote_ja_loppunut_tuote_tilisiirto_oikeilla_tiedoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def _luo_mockit(self):
        pankki = Mock()
        viite = Mock()
        viite.uusi.return_value = 42
        varasto = Mock()
        tuotteet = {1: Tuote(1, "maito", 5), 2: Tuote(2, "leipä", 3)}
        varasto.saldo.side_effect = lambda tuote_id: 10
        varasto.hae_tuote.side_effect = lambda tuote_id: tuotteet[tuote_id]
        return pankki, viite, varasto

    def test_aloita_asiointi_nollaa_edellisen_ostoksen(self):
        pankki, viite, varasto = self._luo_mockit()
        kauppa = Kauppa(varasto, pankki, viite)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 3)

    def test_jokaiselle_maksulle_pyydetaan_uusi_viite(self):
        pankki, viite, varasto = self._luo_mockit()
        viite.uusi.side_effect = [1, 2]
        kauppa = Kauppa(varasto, pankki, viite)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(viite.uusi.call_count, 2)
        self.assertEqual(pankki.tilisiirto.call_args_list[0][0][1], 1)
        self.assertEqual(pankki.tilisiirto.call_args_list[1][0][1], 2)

    def test_korista_poistettu_tuote_ei_nay_hinnassa(self):
        pankki, viite, varasto = self._luo_mockit()
        kauppa = Kauppa(varasto, pankki, viite)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("pekka", "12345")

        varasto.palauta_varastoon.assert_called()
        pankki.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 3)
