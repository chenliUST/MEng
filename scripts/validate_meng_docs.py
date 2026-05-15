from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs" / "ai-native-systems-transformation-meng"

EXPECTED_FILES = [
    PACKAGE / "README.md",
    PACKAGE / "00-proposal-narrative.md",
    PACKAGE / "01-competency-model-and-rubric.md",
    PACKAGE / "02-student-personas-and-bridging.md",
    PACKAGE / "03-curriculum-map.md",
    PACKAGE / "04-course-and-workshop-designs.md",
    PACKAGE / "05-pbl-studio-and-gate-system.md",
    PACKAGE / "06-ai-operating-discipline.md",
    PACKAGE / "07-industry-partnership-and-coop-model.md",
    PACKAGE / "08-assessment-portfolio-and-defense.md",
    PACKAGE / "09-launch-roadmap-and-governance.md",
    ROOT / "docs" / "superpowers" / "specs" / "2026-05-13-ai-native-systems-transformation-meng-design.md",
    ROOT / "docs" / "superpowers" / "plans" / "2026-05-14-ai-native-systems-transformation-meng-program.md",
]

REQUIRED_ANCHORS = {
    PACKAGE / "00-proposal-narrative.md": [
        "AI-Native Systems Transformation",
        "Design practical transformation",
        "use and evaluate AI with professional discipline where it creates responsible value",
    ],
    PACKAGE / "01-competency-model-and-rubric.md": [
        "Systems Understanding And Diagnosis",
        "Transformation Design And Implementation",
        "AI, Data, And Digital Enablement",
        "Professional Judgment And Continuous Learning",
        "Cross-Cutting Thread: Human, Organizational, And Stakeholder Integration",
        "AI/Data Systems Enablement",
    ],
    PACKAGE / "02-student-personas-and-bridging.md": [
        "AI-Strong Technologist",
        "Domain/Engineering Practitioner",
        "Systems/Operations Thinker",
        "Design/Product/Change-Oriented Integrator",
    ],
    PACKAGE / "03-curriculum-map.md": [
        "credit-bearing",
        "Field Implementation / Co-op Residency",
    ],
    PACKAGE / "04-course-and-workshop-designs.md": [
        "Field Seminar",
        "Human-AI Work Design",
    ],
    PACKAGE / "05-pbl-studio-and-gate-system.md": [
        "gate review",
        "Gate 1: Challenge Commitment",
    ],
    ROOT / "docs" / "superpowers" / "specs" / "2026-05-13-ai-native-systems-transformation-meng-design.md": [
        "systems-first, implementation-centered, AI/data-enabled",
        "Systems Understanding And Diagnosis",
        "Transformation Design And Implementation",
        "AI, Data, And Digital Enablement",
        "Cross-Cutting Human, Organizational, And Stakeholder Integration",
    ],
    ROOT / "docs" / "superpowers" / "plans" / "2026-05-14-ai-native-systems-transformation-meng-program.md": [
        "Revision note: after review, the competency model was rebalanced",
    ],
}

UNFINISHED_PATTERN = re.compile(r"\b(TODO|TBD|FIXME|XXX|PLACEHOLDER)\b|\[\[|<TODO", re.IGNORECASE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    failures = []

    for path in EXPECTED_FILES:
        if not path.exists():
            failures.append(f"Missing expected file: {path.relative_to(ROOT)}")

    for path, anchors in REQUIRED_ANCHORS.items():
        if not path.exists():
            continue
        text = read_text(path)
        for anchor in anchors:
            if anchor not in text:
                failures.append(f"Missing anchor in {path.relative_to(ROOT)}: {anchor}")

    for path in EXPECTED_FILES:
        if not path.exists() or path.suffix.lower() != ".md":
            continue
        text = read_text(path)
        for match in UNFINISHED_PATTERN.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            failures.append(f"Unfinished marker in {path.relative_to(ROOT)}:{line_no}: {match.group(0)}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print("MEng document validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
