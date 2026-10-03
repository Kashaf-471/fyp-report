"""Mechanical Phase 2 split and fidelity checks; no report content generation."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "Report template"
BASE = REPORT / "baseline"
MANIFEST = ROOT / ".phase2" / "split_manifest.json"
NAMES = {"A": "Kashaf Ali", "B": "Fatima Malik", "C": "Eesha Irfan"}
CHAPTERS = [
    ("Introduction", "01_introduction.tex", "A"),
    ("Project Vision", "02_project_vision.tex", "A"),
    ("Literature Review / Related Work", "03_literature_review.tex", "B"),
    ("Software Requirement Specifications", "04_software_requirement_specifications.tex", "A"),
    ("Proposed Approach and Methodology", "05_proposed_approach_and_methodology.tex", "B"),
    ("High-Level and Low-Level Design", "06_high_level_and_low_level_design.tex", "C"),
    ("Implementation and Test Cases", "07_implementation_and_test_cases.tex", "C"),
    ("User Manual", "08_user_manual.tex", "A"),
    ("Experimental Results and Discussion", "09_experimental_results_and_discussion.tex", "B"),
    ("Conclusions", "10_conclusions.tex", "A"),
    ("First Appendix if Required", "appendix_a_template_examples.tex", "A"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def original_files():
    return sorted(p for p in (BASE / "sources").rglob("*") if p.is_file())


def snapshot_manifest():
    hashes = {p.relative_to(BASE / "sources").as_posix(): sha(p.read_bytes())
              for p in original_files()}
    for rel, expected in hashes.items():
        assert sha((REPORT / rel).read_bytes()) == expected, f"Original changed: {rel}"
    (BASE / "source_hashes.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
    return hashes


def split():
    assert (BASE / "build" / "main.pdf").is_file(), "Compile original template before splitting."
    assert not MANIFEST.exists(), "Already split: do not refactor main.tex again."
    assert not (REPORT / "chapters").exists(), "Existing chapter files require review."
    assert not (REPORT / "frontmatter").exists(), "Existing front matter files require review."
    hashes = snapshot_manifest()
    original = (REPORT / "main.tex").read_bytes()
    newline = b"\r\n" if b"\r\n" in original else b"\n"
    hits = list(re.finditer(rb"(?m)^\\chapter\{([^\r\n]*)\}", original))
    assert [m.group(1).decode("utf-8") for m in hits] == [c[0] for c in CHAPTERS]
    bib_begin = re.search(rb"(?m)^\{\r?\n\\bibliographystyle\{ieeetr\}", original)
    assert bib_begin and hits[9].start() < bib_begin.start() < hits[10].start()
    document_end = original.index(b"\\end{document}", hits[-1].start())
    blocks = []
    for i, (title, filename, owner) in enumerate(CHAPTERS):
        start = hits[i].start()
        end = bib_begin.start() if i == 9 else document_end if i == 10 else hits[i + 1].start()
        blocks.append((start, end, "chapters/" + filename, owner))
    for heading, filename, owner in [
        ("Abstract", "abstract.tex", "B"),
        ("Executive Summary", "executive_summary.tex", "A"),
    ]:
        marker = ("\\section*{" + heading + "}").encode()
        heading_start = original.index(marker)
        body_start = original.index(b"\n", heading_start) + 1
        body_end = original.index(b"\\pagebreak", body_start)
        blocks.append((body_start, body_end, "frontmatter/" + filename, owner))
    assembled = original
    details = []
    for start, end, rel, owner in sorted(blocks, reverse=True):
        body = original[start:end]
        assert body.endswith(b"\n"), f"Non-line boundary: {rel}"
        header = (f"% Owner: Member {owner} ({NAMES[owner]}); mapping assumed from proposal order.").encode() + newline
        path = REPORT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(header + body)
        input_line = ("\\input{" + rel.removesuffix(".tex") + "}%").encode() + newline
        assembled = assembled[:start] + input_line + assembled[end:]
        details.append({"file": rel, "owner": owner, "name": NAMES[owner],
                        "body_sha256": sha(body), "header_bytes": len(header)})
    assert assembled.count(b"\\bibliography{fypbib}") == 1
    assembled = assembled.replace(b"\\bibliography{fypbib}", b"\\bibliography{fypbib_A,fypbib_B,fypbib_C}")
    for owner in NAMES:
        path = REPORT / f"fypbib_{owner}.bib"
        assert not path.exists(), f"Existing bibliography: {path}"
        header = (f"% Owner: Member {owner} ({NAMES[owner]})." ).encode() + newline
        if owner == "A":
            content = header + b"% Original template entries preserved verbatim for the baseline comparison." + newline + (REPORT / "fypbib.bib").read_bytes()
        else:
            content = header + b"% Reserved for this member's verified project references during a later writing phase." + newline
        path.write_bytes(content)
    (REPORT / "main.tex").write_bytes(assembled)
    manifest = {"original_hashes": hashes, "main_sha256": sha(assembled),
                "files": sorted(details, key=lambda x: x["file"])}
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    verify_sources()
    print("Extracted 10 chapters, unchanged demo appendix, and two summary bodies.")
    print("Created three member bibliographies; original sample entries retained in A.")


def verify_frozen():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert sha((REPORT / "main.tex").read_bytes()) == manifest["main_sha256"], "Frozen main.tex changed."
    assert sha((REPORT / "FastFyp.cls").read_bytes()) == manifest["original_hashes"]["FastFyp.cls"], "Protected FastFyp.cls changed."
    print("PASS: main.tex and FastFyp.cls match their frozen hashes.")


def verify_sources():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    main = (REPORT / "main.tex").read_bytes()
    assert sha(main) == manifest["main_sha256"], "Frozen main.tex changed."
    reconstructed = main
    for item in manifest["files"]:
        raw = (REPORT / item["file"]).read_bytes()
        body = raw[item["header_bytes"]:]
        assert sha(body) == item["body_sha256"], f"Extracted body changed: {item['file']}"
        directive = ("\\input{" + item["file"].removesuffix(".tex") + "}").encode()
        pattern = re.escape(directive) + rb"%?\r?\n"
        assert len(re.findall(pattern, reconstructed)) == 1
        reconstructed = re.sub(pattern, lambda _: body, reconstructed)
    reconstructed = reconstructed.replace(b"\\bibliography{fypbib_A,fypbib_B,fypbib_C}", b"\\bibliography{fypbib}")
    assert reconstructed == (BASE / "sources" / "main.tex").read_bytes(), "Expanded source differs from original."
    for rel, expected in manifest["original_hashes"].items():
        if rel != "main.tex":
            assert sha((REPORT / rel).read_bytes()) == expected, f"Protected source/asset changed: {rel}"
    original_bib = (BASE / "sources" / "fypbib.bib").read_bytes()
    assert (REPORT / "fypbib_A.bib").read_bytes().endswith(original_bib)
    combined = b"".join((REPORT / f"fypbib_{owner}.bib").read_bytes() for owner in NAMES)
    keys = re.findall(rb"@\w+\s*\{\s*([^,]+),", combined)
    original_keys = re.findall(rb"@\w+\s*\{\s*([^,]+),", original_bib)
    assert keys == original_keys and len(set(keys)) == len(keys)
    print("PASS: expanded main.tex reproduces original bytes; class, bibliography and all figures unchanged.")


def warnings(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    found = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if "Warning:" in line or line.startswith(("Overfull ", "Underfull ", "Warning--", "!")):
            block = [line]
            i += 1
            while i < len(lines) and lines[i].strip():
                block.append(lines[i])
                i += 1
            found.append("\n".join(block))
        i += 1
    return found


def compare():
    sys.path.insert(0, str(ROOT / ".phase2/tools/python"))
    import pymupdf
    from PIL import Image, ImageDraw
    verify_sources()
    old_path = BASE / "original-template.pdf"
    new_path = REPORT / "build/main.pdf"
    old = pymupdf.open(old_path)
    new = pymupdf.open(new_path)
    assert len(old) == len(new), "Page count changed."
    differences = []
    page_results = []
    renders = ROOT / ".phase2/verification"
    renders.mkdir(parents=True, exist_ok=True)
    for i in range(len(old)):
        a, b = old[i], new[i]
        same_text = a.get_text("text") == b.get_text("text")
        same_geometry = a.rect == b.rect and a.get_text("words") == b.get_text("words")
        pa = a.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
        pb = b.get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
        same_pixels = (pa.width, pa.height, pa.samples) == (pb.width, pb.height, pb.samples)
        annotations_a = a.get_links()
        annotations_b = b.get_links()
        def links(items):
            return [{k: v for k, v in x.items() if k not in ("xref", "id")} for x in items]
        same_links = links(annotations_a) == links(annotations_b)
        page_results.append({"page": i + 1, "text_equal": same_text,
                             "geometry_equal": same_geometry, "pixels_equal_144dpi": same_pixels,
                             "links_equal": same_links, "render_sha256": sha(pa.samples)})
        if not all((same_text, same_geometry, same_pixels, same_links)):
            differences.append(page_results[-1])
            pa.save(renders / f"difference_{i + 1:03}_original.png")
            pb.save(renders / f"difference_{i + 1:03}_split.png")
    assert (BASE / "build/main.bbl").read_bytes() == (REPORT / "build/main.bbl").read_bytes(), "Bibliography output changed."
    list_files = ["main.toc", "main.lof", "main.lot"]
    list_comparison = {}
    for filename in list_files:
        a, b = BASE / "build" / filename, REPORT / "build" / filename
        list_comparison[filename] = a.exists() and b.exists() and a.read_bytes() == b.read_bytes()
        assert list_comparison[filename], f"Generated list differs: {filename}"
    selected = sorted(set([0, 2, 3, 4, 5, len(new) // 2, len(new) - 3, len(new) - 1]))
    thumbs = []
    for i in selected:
        pix = new[i].get_pixmap(matrix=pymupdf.Matrix(1, 1), alpha=False)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img.thumbnail((360, 510))
        panel = Image.new("RGB", (380, 550), "#dddddd")
        panel.paste(img, ((380 - img.width) // 2, 28))
        ImageDraw.Draw(panel).text((10, 8), f"PDF page {i + 1}", fill="black")
        thumbs.append(panel)
        if i in [3, len(new) // 2]:
            new[i].get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(renders / f"sample_page_{i + 1:03}.png")
    montage = Image.new("RGB", (380 * 4, 550 * ((len(thumbs) + 3) // 4)), "white")
    for j, panel in enumerate(thumbs):
        montage.paste(panel, ((j % 4) * 380, (j // 4) * 550))
    montage.save(renders / "comparison_contact_sheet.png")
    output = {"engine": "Tectonic 0.17.0 (XeTeX with automatic BibTeX/reruns)",
              "original_pdf": str(old_path.relative_to(ROOT)), "split_pdf": str(new_path.relative_to(ROOT)),
              "page_count": len(old), "differences": differences, "pages": page_results,
              "list_files_byte_equal": list_comparison, "bibliography_byte_equal": True,
              "original_warnings": warnings(BASE / "build/main.log"),
              "split_warnings": warnings(REPORT / "build/main.log"),
              "main_tex_frozen_sha256": sha((REPORT / "main.tex").read_bytes())}
    (renders / "comparison.json").write_text(json.dumps(output, indent=2, default=str) + "\n", encoding="utf-8")
    (REPORT / "main.pdf").write_bytes(new_path.read_bytes())
    (BASE / "original-template.pdf").write_bytes(old_path.read_bytes())
    print(f"Compared {len(old)} pages at 144 DPI. Differences: {len(differences)}")
    print("Bibliography and generated TOC/LOF/LOT are byte-identical.")
    print("Contact sheet:", renders / "comparison_contact_sheet.png")
    print("Verification:", renders / "comparison.json")
    assert not differences, "PDFs differ: inspect comparison evidence before completion."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["split", "freeze", "verify", "compare"])
    args = parser.parse_args()
    {"split": split, "freeze": verify_frozen, "verify": verify_sources, "compare": compare}[args.action]()
