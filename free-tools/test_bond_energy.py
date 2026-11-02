import importlib.util
import pathlib
import unittest

spec = importlib.util.spec_from_file_location("bond_energy_estimator", pathlib.Path(__file__).with_name("bond_energy_estimator.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class BondEnergyTests(unittest.TestCase):
    def test_valid_calculation(self):
        self.assertAlmostEqual(m.bond_specific_energy(12, 10000, 100), 10.8)

    def test_feed_product_order(self):
        for feed, product in [(100, 100), (10, 100)]:
            with self.assertRaises(ValueError):
                m.bond_specific_energy(12, feed, product)

    def test_invalid_inputs(self):
        for bad in (0, -1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                m.bond_specific_energy(bad, 1000, 100)

    def test_finer_product_requires_more_energy(self):
        self.assertGreater(m.bond_specific_energy(12, 10000, 60),
                           m.bond_specific_energy(12, 10000, 100))


if __name__ == "__main__":
    unittest.main()
