import os

def extract_final_energy_line(file_path):
    """Extract the final '!    total energy' line from a Quantum ESPRESSO output file."""
    energy_line = None
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip().startswith('!') and 'total energy' in line:
                energy_line = line.strip()
    return energy_line

def search_and_extract_energies_sorted(base_dir='.', output_file='energy.txt'):
    vc_out_paths = []

    # Walk and collect all paths containing 'vc.out'
    for root, dirs, files in os.walk(base_dir):
        if 'vc.out' in files:
            vc_out_paths.append(os.path.join(root, 'vc.out'))

    # Sort the paths alphabetically
    vc_out_paths.sort()

    # Extract and write energy data
    with open(output_file, 'w') as out_f:
        for vc_out in vc_out_paths:
            energy_line = extract_final_energy_line(vc_out)
            if energy_line:
                out_f.write(f"{os.path.dirname(vc_out)}/\n")
                out_f.write(f"{energy_line}\n\n")

    print(f"Sorted energy data written to: {output_file}")

# --- Run it ---
if __name__ == "__main__":
    search_and_extract_energies_sorted(base_dir='.')
