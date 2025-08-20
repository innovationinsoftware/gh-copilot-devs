from __future__ import annotations
from dataclasses import dataclass
import math

MU_EARTH = 3.986004418e14
R_EARTH = 6_371_000
G0 = 9.80665

@dataclass(frozen=True)
class AstroMath:
    @staticmethod
    def escape_velocity(altitude_m: float) -> float:
        r = R_EARTH + altitude_m
        return math.sqrt(2.0 * MU_EARTH / r)

    @staticmethod
    def propellant_needed(delta_v: float, isp_s: float, dry_mass_kg: float) -> float:
        if isp_s <= 0 or dry_mass_kg <= 0:
            raise ValueError("Isp and dry mass must be positive.")
        mf = dry_mass_kg
        m0 = mf * math.exp(delta_v / (G0 * isp_s))
        return m0 - mf

class MissionPlanner:
    def __init__(self, altitude_m: float, isp_s: float, dry_mass_kg: float, loss_margin: float = 0.15):
        self.altitude_m = altitude_m
        self.isp_s = isp_s
        self.dry_mass_kg = dry_mass_kg
        self.loss_margin = loss_margin

    def fuel_to_escape(self) -> tuple[float, float, float]:
        v_escape = AstroMath.escape_velocity(self.altitude_m)
        dv = v_escape * (1.0 + self.loss_margin)
        fuel = AstroMath.propellant_needed(dv, self.isp_s, self.dry_mass_kg)
        return v_escape, dv, fuel