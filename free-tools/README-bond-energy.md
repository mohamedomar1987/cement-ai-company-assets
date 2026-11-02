# Free Bond grinding-energy estimator

**Infinity for Cement Organization** | [Technical explanation and Bond Work Index guide](https://www.cementequipment.org/home/whats-work-index/)

This is a dependency-free Python 3 command-line example for a **preliminary** Bond grinding-energy calculation. It can be reused for educational or early engineering comparisons; it is not a substitute for laboratory testing or a validated mill-sizing study.

## Run

```bash
python3 bond_energy_estimator.py --wi 12 --f80 10000 --p80 100 --tph 50
```

Example output:

```json
{
  "bond_specific_energy_kwh_per_t": 10.8,
  "method": "Bond energy equation; indicative, assumes a compatible Wi basis",
  "idealized_grinding_power_kw": 540.0
}
```

**Inputs:** `--wi` is a *measured* Bond Work Index on a consistent mass basis, `--f80` and `--p80` are the feed and product 80%-passing sizes **in micrometres** (F80 > P80), and `--tph` is optional throughput in metric tonnes per hour.

The implemented expression is `E = 10 × Wi × (1/√P80 − 1/√F80)`, with F80/P80 in µm. The optional idealized power is `E × throughput`. Wi must have the appropriate energy-per-mass unit for the desired result; the tool does **not** convert between short tons and metric tonnes.

**Technical limitations:** This equation is indicative, and does not adjust for actual circuit efficiency, mill type, ball charge, closed-circuit classification, moisture, feed variability, motor/transmission losses, material grindability differences, or Bond correction factors. Plant process parameters and design power must be independently checked against representative lab tests, established engineering methods and OEM limits. Avoid using arbitrary Wi values to justify purchase decisions.

Source and tests: [Python estimator](bond_energy_estimator.py) and [unit tests](test_bond_energy.py). Run tests with `python3 test_bond_energy.py`.

The original estimator and tests in this folder are provided under the MIT License; this grant does not apply to unrelated third-party resources elsewhere in the repository. No paid subscription is required for the code.
