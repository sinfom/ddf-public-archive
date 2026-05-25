import pathlib
import re

# =========================================================
# CONFIG
# =========================================================

ROOT = pathlib.Path("/Users/mf/Library/CloudStorage/OneDrive-SinfomLtd/DDF-md")

# =========================================================
# HELPERS
# =========================================================

def clean_filename(name):
    """
    Convert filename to kebab-case while preserving prefix (e.g. F3a)
    """
    stem = pathlib.Path(name).stem

    # Replace underscores with spaces
    stem = stem.replace("_", " ")

    # Remove special characters (keep alphanumeric and spaces)
    stem = re.sub(r"[^\w\s\-]", "", stem)

    # Collapse multiple spaces
    stem = re.sub(r"\s+", " ", stem).strip()

    # Convert spaces to hyphens
    stem = stem.replace(" ", "-")

    return stem + ".md"


def derive_title(filename):
    """
    Convert filename to readable title
    """
    stem = pathlib.Path(filename).stem

    # Replace hyphens with spaces
    title = stem.replace("-", " ")

    # Capitalise words (preserve things like F3a)
    words = []
    for w in title.split():
        if re.match(r"^[A-Z0-9]+$", w):
            words.append(w)
        else:
            words.append(w.capitalize())

    return " ".join(words)


def has_header_block(text):
    """
    Detect if file already has our metadata block
    """
    return "repository: DDF" in text and "type: research_note" in text


# =========================================================
# MAIN PROCESS
# =========================================================

renamed = []
updated = []
skipped = []

for file in ROOT.rglob("*.md"):

    # Skip zz folders
    if any(part.startswith("zz.") for part in file.parts):
        continue

    # Skip combined file
    if file.name.lower() == "combined.md":
        continue

    original_path = file
    parent = file.parent

    # -----------------------------------------------------
    # RENAME FILE
    # -----------------------------------------------------

    new_name = clean_filename(file.name)
    new_path = parent / new_name

    if file.name != new_name:
        file.rename(new_path)
        file = new_path
        renamed.append((original_path.name, new_name))

    # -----------------------------------------------------
    # READ CONTENT
    # -----------------------------------------------------

    try:
        text = file.read_text(encoding="utf-8")
    except:
        skipped.append(str(file))
        continue

    # -----------------------------------------------------
    # ADD HEADER IF MISSING
    # -----------------------------------------------------

    if not has_header_block(text):

        title = derive_title(file.name)
        rel_path = file.relative_to(ROOT)
        folder = rel_path.parts[0]

        header = f"# {title}\n\n"
        metadata = (
            f"path: {rel_path}\n"
            f"folder: {folder}\n"
            f"filename: {file.name}\n"
            f"repository: DDF\n"
            f"type: research_note\n\n"
        )

        new_text = header + metadata + text

        file.write_text(new_text, encoding="utf-8")
        updated.append(str(file))

# =========================================================
# SUMMARY
# =========================================================

print("\n==============================")
print("DDF STANDARDISATION COMPLETE")
print("==============================\n")

print(f"Files renamed: {len(renamed)}")
for old, new in renamed:
    print(f"  {old} → {new}")

print(f"\nFiles updated with header: {len(updated)}")
for f in updated:
    print(f"  {f}")

print(f"\nFiles skipped (read issues): {len(skipped)}")
for f in skipped:
    print(f"  {f}")

print("\nDONE\n")