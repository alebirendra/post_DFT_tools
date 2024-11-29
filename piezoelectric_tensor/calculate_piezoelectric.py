# File: calculate_piezoelectric.py

def calculate_piezoelectric_coefficient(delta_p, delta_a, a0):
    """
    Calculate piezoelectric coefficient e_ij.

    Args:
        delta_p (float): Change in polarization (C/m^2).
        delta_a (float): Change in lattice parameter (Bohr).
        a0 (float): Equilibrium lattice parameter (Bohr).

    Returns:
        float: Piezoelectric coefficient e_ij (C/m^2).
    """
    # Calculate strain
    strain = delta_a / a0

    # Calculate piezoelectric coefficient
    piezo_coefficient = delta_p / strain
    return piezo_coefficient

if __name__ == "__main__":
    # Input values
    delta_p = 0.0268  # Change in polarization (C/m^2)
    delta_a = 0.0735  # Change in lattice parameter (Bohr)
    a0 = 7.5          # Equilibrium lattice parameter (Bohr)

    # Calculate piezoelectric coefficient
    e_ij = calculate_piezoelectric_coefficient(delta_p, delta_a, a0)

    # Print the result
    print(f"Piezoelectric Coefficient (e_ij): {e_ij:.3f} C/m^2")
