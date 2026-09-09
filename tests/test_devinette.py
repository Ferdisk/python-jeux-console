"""Tests des trois stratégies de la Devinette."""

import devinette


class TestCoupMoyen:
    """Recherche binaire : le coup joué est le milieu de l'intervalle."""

    def test_milieu_intervalle_complet(self):
        assert devinette.coup_moyen(1, 100) == 50

    def test_milieu_intervalle_reduit(self):
        assert devinette.coup_moyen(51, 100) == 75

    def test_intervalle_reduit_a_une_valeur(self):
        assert devinette.coup_moyen(42, 42) == 42

    def test_convergence_en_moins_de_sept_coups(self):
        """Sur 1-100, la dichotomie doit trouver n'importe quel nombre en <= 7 coups."""
        for cible in range(1, 101):
            inf, sup, coups = 1, 100, 0
            proposition = devinette.coup_moyen(inf, sup)
            while proposition != cible:
                coups += 1
                if proposition < cible:
                    inf = proposition + 1
                else:
                    sup = proposition - 1
                proposition = devinette.coup_moyen(inf, sup)
            assert coups <= 7, f"{cible} a demandé {coups} coups"


class TestCoupFacile:
    def test_reste_dans_les_bornes(self):
        for _ in range(200):
            assert 1 <= devinette.coup_facile(1, 100) <= 100

    def test_intervalle_unitaire(self):
        assert devinette.coup_facile(7, 7) == 7


class TestCoupDifficile:
    def test_reste_dans_les_bornes(self):
        for _ in range(200):
            assert 1 <= devinette.coup_difficile(1, 100) <= 100

    def test_utilise_majoritairement_la_dichotomie(self):
        """La stratégie hybride annonce 80 % de recherche binaire : on vérifie l'ordre de grandeur."""
        milieu = devinette.coup_moyen(1, 100)
        tirages = [devinette.coup_difficile(1, 100) for _ in range(1000)]
        proportion = tirages.count(milieu) / len(tirages)
        assert 0.70 < proportion < 0.90
