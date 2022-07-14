import re
from pathlib import Path

from fontmake.font_project import FontProject
from ufoLib2 import Font

repository_dir = Path(__file__).parent.parent

ufo_path = repository_dir / "src-noto" / "eac-font.ufo"

otl_dir = repository_dir / "hudum-feature"
otl_path = otl_dir / "main.fea"


def main():
    inlined_otl_path = ufo_path / "features.fea"
    include_statement_pattern = re.compile(r"include\((.+)\);\n")
    with inlined_otl_path.open("w") as inlined_otl:
        with otl_path.open() as main_otl:
            for line in main_otl:
                if match := include_statement_pattern.fullmatch(line):
                    included_otl_path = otl_path.parent / match.group(1)
                    inlined_otl.write(included_otl_path.read_text())
                else:
                    inlined_otl.write(line)

    ufo = Font.open(ufo_path)
    ufo.info.familyName = "Draft UTN"

    project = FontProject()
    project.run_from_ufos(
        [ufo],
        output=["otf"],
        remove_overlaps=True,
        output_path=repository_dir / "src-noto" / "res" / "DraftUTN-Regular.otf",
    )


if __name__ == "__main__":
    main()
