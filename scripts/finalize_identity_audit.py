"""Record the final manual identity review without changing source metadata."""
import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    rows = {r["id"]: r for r in csv.DictReader((ROOT / "catalog.csv").open(encoding="utf-8-sig"))}
    pending = json.loads((ROOT / "checks/pdf_manual_review.json").read_text())
    previous = {x['id']:x for x in json.loads((ROOT/'checks/pdf_identity_manual_resolutions.json').read_text())}
    newly_reviewed = {'neurips-2019-14120'}
    assert all(x['id'] in previous or x['id'] in newly_reviewed for x in pending), 'New identity exceptions require manual review.'
    for entry in pending:
        if entry['id'] in previous:assert previous[entry['id']]['sha256']==entry['sha256']
    variants = {
        "2026.acl-long.163": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
        "icml-2019-4183": "Blended Conditional Gradients: The Unconditioning of Conditional Gradients",
        "icml-2019-3866": "Competing Against Equilibria in Zero-Sum Games with Evolving Payoffs",
        "neurips-2018-11742": "Neuronal Capacity",
        "neurips-2021-bGfDnD7xo-v": "A Continuized View on Nesterov Acceleration for Stochastic Gradient Descent and Randomized Gossip",
        "neurips-2022-iBBcRUlOAPR": "Training Compute-Optimal Large Language Models",
    }
    resolutions = []
    for entry in pending:
        row = rows[entry["id"]]
        visual = entry["id"] not in variants
        preview = None
        if visual:
            src = Path("/tmp") / f"paper-verify-{entry['id']}.png"
            dst = ROOT / "checks/manual_identity_previews" / src.name
            dst.parent.mkdir(exist_ok=True)
            if src.exists():
                shutil.copy2(src, dst)
            assert dst.exists(), dst
            preview = str(dst.relative_to(ROOT))
        resolutions.append({
            "id": entry["id"],
            "path": row["local_path"],
            "sha256": entry["sha256"],
            "expected_title": row["title"],
            "observed_pdf_title": variants.get(entry["id"], row["title"]),
            "method": "visual_first_page_title_and_authors" if visual else "first_page_text_title_and_authors",
            "resolution": "identity_confirmed",
            "note_zh": "首页题名和作者经目视核对一致；字体编码导致自动提取失败。" if visual else "会议元数据与 PDF 使用不同题名；首页作者一致，已核对论文身份，保留原始会议题名。",
            "preview": preview,
        })
    assert len(resolutions) == len(pending)
    write_json(ROOT / "checks/pdf_identity_manual_resolutions.json", resolutions)
    validation_path = ROOT / "checks/validation_summary.json"
    validation = json.loads(validation_path.read_text())
    validation["manual_identity_checks_resolved"] = len(resolutions)
    validation["unresolved_identity_checks"] = 0
    write_json(validation_path, validation)

    # Remove only a generated file explicitly listed as unused in the final catalog.
    manifest_path = ROOT / "checks/unselected_generated_pdf_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    selected = {r["local_path"] for r in rows.values() if r["local_path"]}
    for entry in manifest:
        assert entry["path"] not in selected
        path = ROOT / entry["path"]
        assert path.resolve().is_relative_to((ROOT / "pdfs").resolve())
        if path.exists():
            assert path.stat().st_size == entry["bytes"]
            entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            path.unlink()
            entry["removed"] = True
            entry["removed_at"] = datetime.now(timezone.utc).isoformat()
    write_json(manifest_path, manifest)
    print(json.dumps(validation, ensure_ascii=False))


if __name__ == "__main__":
    main()
