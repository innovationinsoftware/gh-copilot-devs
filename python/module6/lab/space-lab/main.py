from astro import MissionPlanner

def main():
    planner = MissionPlanner(
        altitude_m=200_000,
        isp_s=320.0,
        dry_mass_kg=1200.0,
        loss_margin=0.15
    )
    v_escape, dv, fuel = planner.fuel_to_escape()
    print(f"Escape speed: {v_escape:.0f} m/s")
    print(f"Δv (with margin): {dv:.0f} m/s")
    print(f"Propellant required: {fuel:.0f} kg")

if __name__ == "__main__":
    main()