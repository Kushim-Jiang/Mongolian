from pathlib import Path
from fontmake.font_project import FontProject
from ufoLib2 import Font

from rename import build_mapping_from_yaml, rename_glyphs

directory = Path(__file__).parent
repo_dir = directory.parent
otl_dir = repo_dir / "src"
temp_dir = repo_dir / "temp"


def main():

    temp_dir.mkdir(exist_ok=True)

    ufo = Font.open(directory / "161Source005-cubic.ufo")
    ufo.info.familyName = "Mongolian Baiti"

    # rename glyph
    yaml_dir = directory / "MongolianBaiti.yaml"
    yaml_mapping = build_mapping_from_yaml(yaml_dir)

    translation = {
        'o.AO.init': 'o.AU.init',
        'o.O.medi': 'o.U.medi',
        'o.AO.medi': 'o.AU.medi',
        'u.AO.init': 'u.AU.init',
        'u.U.init': 'u.U.init',
        'u.O.medi': 'u.U.medi',
        'u.AO.medi': 'u.AU.medi',
        'oe.AOI.init': 'oe.AUI.init',
        'oe.O.medi': 'oe.U.medi',
        'oe.OI.medi': 'oe.UI.medi',
        'oe.AOI.medi': 'oe.AUI.medi',
        'ue.AOI.init': 'ue.AUI.init',
        'ue.O.init': 'ue.U.init',
        'ue.O.medi': 'ue.U.medi',
        'ue.OI.medi': 'ue.UI.medi',
        'ue.AOI.medi': 'ue.AUI.medi',
        'bo.BO.init': 'BU.init',
        'bo.BO.medi': 'BU.medi',
        'boe.BOI.init': 'BUI.init',
        'po.PO.init': 'PU.init',
        'po.PO.medi': 'PU.medi',
        'poe.POI.init': 'PUI.init',
        'poe.POI.medi': 'PUI.medi',
        'goe.GOI.init': 'GUI.init',
        'goe.GO.init': 'GU.init',
        'goe.GO.medi': 'GU.medi',
        'goe.GOI.medi': 'GUI.medi',
        'goe.GxOI.init': 'GxUI.init',
        'goe.GxO.init': 'GxU.init',
        'goe.GxO.medi': 'GxU.medi',
        'goe.GxOI.medi': 'GxUI.medi',
        'fo.FO.init': 'FU.init',
        'fo.FO.medi': 'FU.medi',
        'foe.FOI.init': 'FUI.init',
        'foe.FOI.medi': 'FUI.medi',
        'k2o.K2O.init': 'K2U.init',
        'k2o.K2O.medi': 'K2U.medi',
        'k2oe.K2OI.init': 'K2UI.init',
        'k2oe.K2OI.medi': 'K2UI.medi',
        'ko.KO.init': 'KU.init',
        'ko.KO.medi': 'KU.medi',
        'koe.KOI.init': 'KUI.init',
        'koe.KOI.medi': 'KUI.medi',
        'h.Hx.isol': 'h.Gh.isol',
        'h.Hx.init': 'h.Gh.init',
        'h.Hx.medi': 'h.Gh.medi',
        'h.Hx.fina': 'h.Gh.fina',
        'ee.AW.isol': 'eh.AW.isol',
        'ee.AW.init': 'eh.AW.init',
        'ee.W.medi': 'eh.W.medi',
        'ee.W.fina': 'eh.W.fina',
        'b.B2.fina': 'b.Bb.fina',
        's.S2.fina': 's.Ss.fina'
    }
    yaml_mapping.update({k: x for k, v in yaml_mapping.items() if (x := translation.get(v))})
    rename_glyphs(ufo, yaml_mapping)

    for greg_name, utn_name in yaml_mapping.items():
        if greg_name.startswith("uni") and "." in utn_name:  # UTN Mongolian variants that have a uni name in Greg’s glyph set

            glyph = ufo[utn_name]
            unicodes = glyph.unicodes.copy()
            glyph.unicodes.clear()

            letter, *_ = utn_name.split(".")
            cmap_glyph = ufo.newGlyph(f"{letter}-mon")
            cmap_glyph.unicodes = unicodes

    for constructed, origin in {
            "oe.AU.isol": "ue.AU.isol",
            "n.A.isol": "n.A.init",  # should be n.isol
            'sh.S.isol': 's.S.isol',
            'sh.S.init': 's.S.init',
            'sh.S.medi': 's.S.medi',
            'd.T.isol': 't.T.isol',
            'j.I2.isol': 'i.I.init',  # should be j.isol
            'y.I.isol': 'i.I.init',  # should be y.isol
            'y.II.medi': 'i.II.medi',
            'w.U.medi': 'u.U.medi',
    }.items():
        ufo[constructed] = ufo[origin].copy()

    for name in ["zwnj", "zwj", "mvs.effe", "nnbsp.effe", 'fvs1.effe', 'fvs2.effe', 'fvs3.effe', 'fvs4.effe']:  # TODO, FIXME
        ufo.newGlyph(name)

    # feature
    for path in otl_dir.iterdir():
        if path.suffix == ".fea":
            (temp_dir / path.name).write_text(path.read_text())

    lines = [
        "include(main.fea);\n",
        "feature dist {\n",
    ]
    lines.extend(f"    pos {i} {ufo[i].width};\n" for i in ["nirugu", "fvs1", "fvs2", "fvs3", "fvs4"])
    lines.append("} dist;\n")

    ufo.features.text = "".join(lines)

    path = temp_dir / "font.ufo"
    ufo.save(path, overwrite=True)  # fontmake reads fro

    project = FontProject()
    project.run_from_ufos(str(path), output=["otf"], remove_overlaps=True, output_path=directory / "Baiti-Regular.otf")


if __name__ == "__main__":
    main()
