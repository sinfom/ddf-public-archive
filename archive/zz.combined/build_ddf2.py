import pathlib
import re
from datetime import datetime
from collections import defaultdict

# =========================================================
# CONFIG
# =========================================================

ROOT = pathlib.Path("/Users/mf/Library/CloudStorage/OneDrive-SinfomLtd/DDF-md")

OUT_DIR = ROOT / "zz.combined"
OUT_DIR.mkdir(exist_ok=True)

INDEX_DIR = ROOT / "00_index"
INDEX_DIR.mkdir(exist_ok=True)

COMBINED_CURRENT = ROOT / "combined.md"
TIMESTAMP = datetime.now().strftime("%y%m%d.%H%M")
COMBINED_ARCHIVE = OUT_DIR / f"{TIMESTAMP}.Combined.md"

FOLDER_ORDER = [
    "01_foundations",
    "02_operator_notes",
    "03_geometry",
    "04_action_principle",
    "05_gravity_limit",
    "06_quantum_structure",
    "07_Number_Theory",
    "08_figures",
    "09_progress_numeric_projection",
    "10_notes_Papers",
]

# =========================================================
# FILE COLLECTION
# =========================================================

def collect_files():
    files = []

    for file in ROOT.rglob("*.md"):

        if any(part.startswith("zz.") for part in file.parts):
            continue

        if file.name.endswith(".Combined.md"):
            continue

        if file.name == "combined.md":
            continue

        if "00_index" in file.parts:
            continue

        if "template" in file.name.lower():
            continue

        if "_index.md" in file.name:
            continue

        files.append(file)

    return files


# =========================================================
# SORTING
# =========================================================

def sort_files(files):

    def sort_key(f):
        rel = f.relative_to(ROOT)
        folder = rel.parts[0]

        try:
            folder_index = FOLDER_ORDER.index(folder)
        except ValueError:
            folder_index = 999

        return (folder_index, str(rel).lower())

    return sorted(files, key=sort_key)


# =========================================================
# METADATA EXTRACTION
# =========================================================

def extract_metadata(file):

    text = file.read_text(encoding="utf-8", errors="ignore")

    note_id = None
    title = None
    depends = []

    # --- Try extract from content ---
    m = re.search(r"# Note ID\s*\n\s*(.+)", text, re.IGNORECASE)
    if m:
        note_id = m.group(1).strip()

    m = re.search(r"# Title\s*\n\s*(.+)", text, re.IGNORECASE)
    if m:
        title = m.group(1).strip()

    # --- Fallback: extract from filename ---
    if not note_id:
        fname = file.stem
        m = re.match(r"([A-Z]+[0-9]+[a-zA-Z]*)", fname)
        if m:
            note_id = m.group(1)

    if not title:
        fname = file.stem
        title = fname.replace("-", " ").capitalize()

    # --- Dependencies ---
    matches = re.findall(r"Depends On(.*?)(\n#|\Z)", text, re.IGNORECASE | re.DOTALL)

    for match in matches:
        block = match[0]
        lines = block.split("\n")

        for line in lines:
            line = line.strip()
            line = re.sub(r"^[-•\*]\s*", "", line)

            if not line:
                continue

            tokens = re.findall(r"\b[NPGQT][A-Z\-0-9]*\d+\b", line)

            if tokens:
                depends.extend(tokens)
            elif len(line) < 80:
                depends.append(line)

    depends = list(set(depends))

    return note_id, title, depends

# =========================================================
# METADATA CACHE
# =========================================================

_metadata_cache = {}

def get_metadata(file):
    if file not in _metadata_cache:
        _metadata_cache[file] = extract_metadata(file)
    return _metadata_cache[file]

# =========================================================
# COMBINED FILE
# =========================================================
def write_output(path, files):
    with open(path, "w", encoding="utf-8") as out:
        out.write("# DDF Combined Markdown\n\n")
        out.write(f"Generated: {datetime.now()}\n\n")

        current_folder = None

        for f in files:
            rel = f.relative_to(ROOT)
            folder = rel.parts[0]

            if folder != current_folder:
                out.write(f"\n\n# {folder}\n\n")
                current_folder = folder

            note_id, title, depends = get_metadata(f)

            out.write("\n---\n")
            out.write(f"FILE: {rel}\n")

            if note_id:
                out.write(f"ID: {note_id}\n")

            if title:
                out.write(f"TITLE: {title}\n")

            if depends:
                out.write(f"DEPENDS: {', '.join(depends)}\n")

            out.write("---\n\n")

            try:
                out.write(f.read_text(encoding="utf-8", errors="ignore"))
            except Exception as e:
                out.write(f"[ERROR: {e}]\n")

            out.write("\n")


def build_combined(files):
    files = sort_files(files)
    write_output(COMBINED_CURRENT, files)
    write_output(COMBINED_ARCHIVE, files)
    print("Combined.md built")


# =========================================================
# AI CONTEXT INDEX
# =========================================================

def build_ai_context_index(files):

    out_file = INDEX_DIR / "ai_context_index.md"
    files = sort_files(files)

    with open(out_file, "w", encoding="utf-8") as out:

        out.write("# AI Context Index\n\n")

        current_folder = None

        for f in files:

            rel = f.relative_to(ROOT)
            folder = rel.parts[0]

            if folder != current_folder:
                out.write(f"\n## {folder}\n\n")
                current_folder = folder

            note_id, title, _ = get_metadata(f)

            label = note_id if note_id else rel.name
            if title:
                label += f" — {title}"

            out.write(f"- {label}\n")

    print("AI context index built")


# =========================================================
# MASTER INDEX
# =========================================================

def build_master_index(files):

    out_file = INDEX_DIR / "master_index.md"
    files = sort_files(files)

    counts = {}
    for f in files:
        top = f.relative_to(ROOT).parts[0]
        counts[top] = counts.get(top, 0) + 1

    total = len(files)

    with open(out_file, "w", encoding="utf-8") as out:

        out.write("# Master Index\n\n")

        out.write("## Repository Metrics\n\n")
        out.write(f"- Total notes: {total}\n\n")

        out.write("## Repository Structure\n\n")
        out.write("| Folder | Notes |\n")
        out.write("|--------|------|\n")

        for k in sorted(counts):
            out.write(f"| {k} | {counts[k]} |\n")

    print("Master index built")


# =========================================================
# DEPENDENCY GRAPH
# =========================================================

def build_dependency_graph(files):

    out_file = INDEX_DIR / "dependency_graph.md"
    files = sort_files(files)

    # Single pass — cache handles repeated calls
    graph = {}
    known_ids = set()

    for f in files:
        note_id, title, depends = get_metadata(f)
        rel = f.relative_to(ROOT)
        if note_id:
            known_ids.add(note_id)
        key = note_id if note_id else rel.name
        graph[key] = depends

    with open(out_file, "w", encoding="utf-8") as out:
        out.write("# Dependency Graph\n\n")

        for node, deps in graph.items():
            out.write(f"## {node}\n")

            if deps:
                for d in deps:
                    if d not in known_ids:
                        out.write(f"- ⚠ missing → {d}\n")
                    else:
                        out.write(f"- depends on → {d}\n")
            else:
                out.write("- no dependencies\n")

            out.write("\n")

        out.write("\n---\n\n")
        out.write("## Visual Graph\n\n")
        out.write("```mermaid\n")
        out.write("graph TD\n")

        for node, deps in graph.items():
            for d in deps:
                if d in known_ids:
                    out.write(f"    {node} --> {d}\n")

        out.write("```\n")

    print("Dependency graph built")

# =========================================================
# FOLDER INDEXES
# =========================================================

def build_folder_indexes(files):

    folder_map = defaultdict(list)

    for f in files:
        rel = f.relative_to(ROOT)
        top = rel.parts[0]
        folder_map[top].append(f)

    for folder, folder_files in folder_map.items():

        if folder == "00_index":
            continue

        folder_path = ROOT / folder
        index_name = f"{folder}_index.md"
        out_file = folder_path / index_name

        with open(out_file, "w", encoding="utf-8") as out:

            out.write(f"# {folder} Index\n\n")

            out.write("## Files\n\n")

            # Sort by ID (important)
            sorted_files = sorted(folder_files, key=lambda x: get_metadata(x)[0] or "")

            for f in sorted_files:

                rel = f.relative_to(ROOT)

                note_id, title, depends = get_metadata(f)

                label = note_id if note_id else f.name
                if title:
                    label += f" — {title}"

                out.write(f"- {label}\n")

                if depends:
                    for d in depends:
                        out.write(f"    - depends on → {d}\n")

            out.write("\n## Subfolders\n\n")

            for sub in sorted(folder_path.rglob("*")):

                if not sub.is_dir():
                    continue

                if sub == folder_path:
                    continue

                if any(p.startswith("zz.") for p in sub.parts):
                    continue

                rel = sub.relative_to(folder_path)
                out.write(f"- {rel}/\n")

        print(f"{index_name} built")


# =========================================================
# MAIN
# =========================================================

def main():

    print("Scanning files...")
    files = collect_files()
    print(f"Files found: {len(files)}")

    print("\nBuilding combined...")
    build_combined(files)

    print("\nBuilding AI index...")
    build_ai_context_index(files)

    print("\nBuilding master index...")
    build_master_index(files)

    print("\nBuilding dependency graph...")
    build_dependency_graph(files)

    print("\nBuilding folder indexes...")
    build_folder_indexes(files)

    print("\nDONE")


if __name__ == "__main__":
    main()