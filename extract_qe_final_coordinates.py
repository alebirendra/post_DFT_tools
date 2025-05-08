import re

def extract_final_block(lines, keyword):
    """Extract the final block starting with the given keyword (e.g., CELL_PARAMETERS)."""
    blocks = []
    block = []
    recording = False

    for line in lines:
        if keyword in line:
            if block:
                blocks.append(block)
                block = []
            recording = True
            block.append(line)
        elif recording:
            if line.strip() == '' or not re.match(r'\s*\S+', line):
                recording = False
                blocks.append(block)
                block = []
            elif 'End final coordinates' in line:
                continue  # Skip comment lines
            else:
                block.append(line)

    if block:
        blocks.append(block)

    if not blocks:
        raise ValueError(f"No block starting with '{keyword}' found.")
    
    return blocks[-1]

def process_qe_files(vc_out_path, vc_in_path, output_path):
    with open(vc_out_path, 'r') as f:
        vc_out_lines = f.readlines()

    with open(vc_in_path, 'r') as f:
        vc_in_lines = f.readlines()

    # Extract final blocks
    final_cell_block = extract_final_block(vc_out_lines, "CELL_PARAMETERS")
    final_coords_block = extract_final_block(vc_out_lines, "ATOMIC_POSITIONS")

    # Find where to remove in vc.in
    new_input = []
    skip = False

    for i, line in enumerate(vc_in_lines):
        if not skip and line.startswith("CELL_PARAMETERS"):
            skip = True  # Start skipping from here
            continue
        if skip and line.strip().startswith("K_POINTS"):
            skip = False  # Stop skipping here
            new_input.append("\n")  # Add spacing before re-inserting
            new_input.extend(final_cell_block)
            new_input.extend(final_coords_block)
            new_input.append("\n")
            new_input.append(line)
            continue
        if not skip:
            new_input.append(line)

    with open(output_path, 'w') as f:
        f.writelines(new_input)

    print(f"Updated input file written to: {output_path}")

# --- Usage ---
vc_out_file = 'vc.out'
vc_in_file = 'vc.in'
output_file = '1vc.in'

process_qe_files(vc_out_file, vc_in_file, output_file)
