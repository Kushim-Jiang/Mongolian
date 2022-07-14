from pathlib import Path
from fontmake.font_project import FontProject
from ufoLib2 import Font

from rename import build_mapping_from_yaml, rename_glyphs

repository_dir = Path(__file__).parent.parent
noto_dir = repository_dir / "src-noto"
res_dir = noto_dir / "res"
temp_dir = noto_dir / "temp"
otl_dir = repository_dir / "hudum-feature"


def main():
    temp_dir.mkdir(exist_ok=True)

    ufo = Font.open(noto_dir / "NotoSansMongolian-Regular.ufo")
    ufo.info.familyName = "Noto Sans Mongolian"

    # rename glyph
    yaml_dir = noto_dir / "NotoSansMongolian.yaml"
    yaml_mapping = build_mapping_from_yaml(yaml_dir)
    rename_glyphs(ufo, yaml_mapping)

    for noto_name, utn_name in yaml_mapping.items():
        if noto_name.startswith("uni") and "." in utn_name:  # UTN Mongolian variants that have a uni name in Greg’s glyph set

            glyph = ufo[utn_name]
            unicodes = glyph.unicodes.copy()
            glyph.unicodes.clear()

            letter, *_ = utn_name.split(".")
            cmap_glyph = ufo.newGlyph(f"{letter}-mon")
            cmap_glyph.unicodes = unicodes

    for constructed, origin in {
            # These 10 glyphs are used by EAC, not used by Baiti
            "a.Aa.fina": ".notdef",
            "e.Aa.fina": ".notdef",
            "i.I.isol": "j.I.isol",
            "i.Ix.isol": ".notdef",
            "i.I.init": "y.I.init",
            "u.U.isol": ".notdef",
            "u.Ux.isol": ".notdef",
            "u.O.init": "ue.O.init",
            "u.O.fina": "o.O.fina",
            "oe.AU.isol": "ue.AU.isol",
            "oe.O.fina": "o.O.fina",
            "ue.U.isol": ".notdef",
            "ue.Ux.isol": ".notdef",
            "ue.O.fina": "o.O.fina",
            "n.A.isol": ".notdef",
            "h.Gh.isol": "g.Gh.isol",
            "h.Gx.init": ".notdef",
            "h.Gx.medi": ".notdef",
            "g.H.isol": "h.H.isol",
            "g.Gx.isol": ".notdef",
            "g.Gx.init": ".notdef",
            "g.Gx.medi": ".notdef",
            "sh.S.isol": "s.S.isol",
            "sh.S.init": "s.S.init",
            "sh.S.medi": "s.S.medi",
            "d.T.isol": "t.T.isol",
            "y.I.isol": "j.I.isol",
            "y.II.medi": "i.II.medi"
    }.items():
        ufo[constructed] = ufo[origin].copy()

    # TODO, FIXME
    for name in ["zwnj", "zwj", "mvs.effe", "nnbsp.effe", 'fvs1.effe', 'fvs2.effe', 'fvs3.effe', 'fvs4.effe']:
        ufo.newGlyph(name)

    # feature
    for path in otl_dir.iterdir():
        if path.suffix == ".fea":
            (temp_dir / path.name).write_text(path.read_text())

    lines = [
        "include(main.fea);\n",
        # "feature dist {\n",
    ]
    # lines.extend(f"    pos {i} {ufo[i].width};\n" for i in ["nirugu", "fvs1", "fvs2", "fvs3", "fvs4"])
    # lines.append("} dist;\n")
    ufo.features.text = "".join(lines)

    path = temp_dir / "font.ufo"
    ufo.save(path, overwrite=True)  # fontmake reads fro

    project = FontProject()
    project.run_from_ufos(
        str(path),
        output=["otf"],
        remove_overlaps=True,
        output_path=noto_dir / "res" / "Baiti-Regular.otf",
    )


if __name__ == "__main__":
    main()
