#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Ruiyi Zhang
"""Copy a reviewable Latin-only repository with provenance, without moving originals."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PDF_NAME = "Methodus inveniendi lineas curvas maximi minimive proprietate gaudentes.pdf"
APPROVED_PDF_SHA256 = "0ec2d3570b1510cd392ac937e0a87d9abd2a4f72cb6cd16ba19f4154037f45e1"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_files():
    files = {ROOT / "tex/e65-complete.tex"}
    pending = list(files)
    while pending:
        path = pending.pop()
        if path.suffix != ".tex":
            continue
        for rel in re.findall(r"\\(?:input|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}", path.read_text()):
            target = (ROOT / "tex" / rel).resolve()
            if not target.suffix:
                target = target.with_suffix(".tex")
            target.relative_to(ROOT / "tex")
            if not target.is_file():
                raise FileNotFoundError(target)
            if target not in files:
                files.add(target)
                pending.append(target)
    root_docs = ["README.md", "PROVENANCE.md", "RIGHTS.md", "PUBLICATION.md", "CONTRIBUTING.md", "CITATION.cff", ".gitignore", ".gitattributes", "requirements.txt", "LICENSE"]
    scripts = ["build-complete.sh", "check-complete.py", "ocr.py", "assemble_ocr.py", "trace_ornament.py", "prepare-public-repo.py"]
    files.update(ROOT / name for name in root_docs)
    files.update(ROOT / "scripts" / name for name in scripts)
    files.update((ROOT / "editorial").glob("*.md"))
    files.update((ROOT / "LICENSES").glob("*.txt"))
    files.add(ROOT / "LICENSES/README.md")
    files.update((ROOT / "sources/e-rara").glob("*"))
    files.update(ROOT / name for name in ["editorial/complete-qa.json", "ocr/full-raw.txt", "ocr/page-manifest.csv", "sources/source-manifest.json", "sources/font-manifest.json", "tex/figures/title-ornament.svg"])
    return sorted(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=ROOT / "publication/euler-methodus-1744")
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination.exists():
        raise FileExistsError(f"Destination already exists; choose a fresh directory: {destination}")
    if destination == ROOT or ROOT.is_relative_to(destination):
        raise ValueError("Destination must not contain the source project")
    files = selected_files()
    if any(not path.is_file() for path in files):
        raise FileNotFoundError("A selected input is missing")
    pdf = ROOT / "output/pdf" / PDF_NAME
    if digest(pdf) != APPROVED_PDF_SHA256:
        raise ValueError("The approved PDF has changed; review the release selection explicitly")
    destination.mkdir(parents=True)
    records = []
    for path in files:
        rel = path.relative_to(ROOT)
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        source_hash = digest(path)
        if digest(target) != source_hash:
            raise ValueError(f"Copy verification failed: {rel}")
        records.append({"path": rel.as_posix(), "bytes": path.stat().st_size, "sha256": source_hash})
    release = destination / "release"
    release.mkdir()
    shutil.copy2(pdf, release / PDF_NAME)
    release_record = {"filename": PDF_NAME, "bytes": pdf.stat().st_size, "sha256": digest(pdf), "pages": 212, "status": "Latin working edition; PDF artifact unchanged from the September 2026 edition"}
    (release / "manifest.json").write_text(json.dumps(release_record, ensure_ascii=False, indent=2) + "\n")
    manifest = {"scope": "Latin working edition; modern editorial and figure code CC-BY-SA-4.0, independent scripts MIT", "files": records, "release": release_record, "excluded": ["original scan PDF", "translation", "ocr/raw", "tmp", "historical proofs and samples", "complete upstream checkout"]}
    (destination / "EXPORT-MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"destination": str(destination), "files": len(records), "source_bytes": sum(record["bytes"] for record in records), "release_sha256": release_record["sha256"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
