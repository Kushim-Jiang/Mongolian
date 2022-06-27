import re
from pathlib import Path

from fontmake.font_project import FontProject
from ufoLib2 import Font

directory = Path(__file__).parent

otl_dir = directory
otl_path = otl_dir / "main.fea"


def main():
    inlined_otl_path = otl_dir / "utn-font.ufo" / "features.fea"
    include_statement_pattern = re.compile(r"include\((.+)\);\n")
    with inlined_otl_path.open("w") as inlined_otl:
        with otl_path.open() as main_otl:
            for line in main_otl:
                if match := include_statement_pattern.fullmatch(line):
                    included_otl_path = otl_path.parent / match.group(1)
                    inlined_otl.write(included_otl_path.read_text())
                else:
                    inlined_otl.write(line)

    # dist
    ufo = Font.open(directory / "utn-font.ufo")
    with inlined_otl_path.open("a") as inlined_otl:
        inlined_otl.write("\n\n")
        inlined_otl.write("feature dist {\n")
        for glyph_name in ["nirugu", "fvs1", "fvs2", "fvs3", "fvs4"]:
            inlined_otl.write("\tpos " + glyph_name + " " + str(ufo[glyph_name].width) + ";\n")
        inlined_otl.write("} dist;")

    ufo = Font.open(directory / "utn-font.ufo")
    ufo.info.familyName = "Draft UTN"

    project = FontProject()
    project.run_from_ufos(
        [ufo],
        output=["otf"],
        remove_overlaps=True,
        output_path=directory.parent / "otf" / "DraftUTN-Regular.otf",
    )


if __name__ == "__main__":
    main()
