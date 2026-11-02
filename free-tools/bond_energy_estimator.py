#!/usr/bin/env python3
"""Illustrative Bond grinding-energy estimator; not a mill-design guarantee.

F80 and P80 are particle-size distributions' 80% passing sizes in micrometres.
Wi must be obtained from a representative Bond work-index test, with unit basis
consistent with the desired kWh per mass unit (for example, metric tonnes).
"""
from __future__ import annotations

import argparse
import json
import math


def bond_specific_energy(wi: float, f80_um: float, p80_um: float) -> float:
    """Calculate E = 10 Wi (1/sqrt(P80) - 1/sqrt(F80)).

    The conventional Bond formulation assumes sizes in micrometres. It does not
    include corrections for circuit efficiency, mill configuration or material
    variations; it is an indicative baseline, not an equipment rating.
    """
    values = {"Wi": wi, "F80": f80_um, "P80": p80_um}
    for name, value in values.items():
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be finite and greater than zero")
    if p80_um >= f80_um:
        raise ValueError("P80 must be smaller than F80 for a grinding duty")
    return 10.0 * wi * (1.0 / math.sqrt(p80_um) - 1.0 / math.sqrt(f80_um))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wi", type=float, required=True, help="Measured Bond work index, e.g. 12")
    parser.add_argument("--f80", type=float, required=True, help="Feed F80 in micrometres")
    parser.add_argument("--p80", type=float, required=True, help="Product P80 in micrometres")
    parser.add_argument("--tph", type=float, help="Optional mass flow in tonnes/hour")
    args = parser.parse_args()
    try:
        e = bond_specific_energy(args.wi, args.f80, args.p80)
        if args.tph is not None and (not math.isfinite(args.tph) or args.tph <= 0):
            raise ValueError("throughput must be finite and greater than zero")
    except ValueError as exc:
        parser.error(str(exc))
    result = {"bond_specific_energy_kwh_per_t": round(e, 4),
              "method": "Bond energy equation; indicative, assumes a compatible Wi basis"}
    if args.tph is not None:
        result["idealized_grinding_power_kw"] = round(e * args.tph, 4)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
