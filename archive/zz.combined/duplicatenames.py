import pathlib
import re
from collections import defaultdict

# =========================================================
# CONFIG
# =========================================================

ROOT = pathlib.Path("/Users/mf/Library/CloudStorage/OneDrive-SinfomLtd/DDF-md")

# =========================================================
# LOGIC
# =========================================================

prefix_map = defaultdict(list)

for file in ROOT.rglob("*.md"):

    # Skip zz folders
    if any(part.startswith("zz.") for part in file.parts):
        continue

    # Skip combined
    if file.name.lower() == "combined.md":
        continue

    name = file.stem

    # Extract prefix like F5, N1, P3a etc.
    match = re.match(r"^([A-Z]\d+[A-Za-z]*)", name)

    if match:
        prefix = match.group(1)
        prefix_map[prefix].append(file.relative_to(ROOT))

# =========================================================
# OUTPUT
# =========================================================

print("\n==============================")
print("DUPLICATE PREFIX REPORT")
print("==============================\n")

duplicates_found = False

for prefix, files in sorted(prefix_map.items()):

    if len(files) > 1:
        duplicates_found = True
        print(f"\n{prefix} → {len(files)} files")
        print("-" * 40)

        for f in files:
            print(f"  {f}")

if not duplicates_found:
    print("No duplicate prefixes found.")

print("\nDONE\n")