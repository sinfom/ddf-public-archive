import pathlib

# =========================================================
# CONFIG
# =========================================================

ROOT = pathlib.Path("/Users/mf/Library/CloudStorage/OneDrive-SinfomLtd/DDF-md")

# =========================================================
# LOGIC
# =========================================================

def list_structure(base, indent=0):

    for item in sorted(base.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):

        # Skip zz folders
        if item.is_dir() and item.name.startswith("zz."):
            continue

        prefix = "    " * indent

        if item.is_dir():
            print(f"{prefix}[DIR]  {item.name}")
            list_structure(item, indent + 1)
        else:
            print(f"{prefix}      {item.name}")


# =========================================================
# RUN
# =========================================================

print("\n==============================")
print("DDF DIRECTORY STRUCTURE")
print("==============================\n")

list_structure(ROOT)

print("\nDONE\n")