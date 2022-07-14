from pathlib import Path
from fontmake.font_project import FontProject
from ufoLib2 import Font

from rename import build_mapping_from_yaml, rename_glyphs

repository_dir = Path(__file__).parent.parent
baiti_dir = repository_dir / "src-baiti"
res_dir = baiti_dir / "res"
temp_dir = baiti_dir / "temp"
otl_dir = repository_dir / "hudum-feature"


def main():
    temp_dir.mkdir(exist_ok=True)

    ufo = Font.open(baiti_dir / "161Source005-cubic.ufo")
    ufo.info.familyName = "Mongolian Baiti"

    # rename glyph
    yaml_dir = baiti_dir / "MongolianBaiti.yaml"
    yaml_mapping = build_mapping_from_yaml(yaml_dir)

    translation = {
        "BA.isol": "b_a.BA.isol",
        "BA.init": "b_a.BA.init",
        "BA.medi": "b_a.BA.medi",
        "BA.fina": "b_a.BA.fina",
        "BI.isol": "b_i.BI.isol",
        "BI.init": "b_i.BI.init",
        "BI.medi": "b_i.BI.medi",
        "BI.fina": "b_i.BI.fina",
        "BO.isol": "b_o.BO.isol",
        "BO.init": "b_o.BO.init",
        "BO.medi": "b_o.BO.medi",
        "BO.fina": "b_o.BO.fina",
        "BUe.isol": "b_oe.BUe.isol",
        "BOI.init": "b_oe.BOI.init",
        "BOI.medi": "b_oe.BOI.medi",
        "BUe.fina": "b_oe.BUe.fina",
        "BW.isol": "b_eh.BW.isol",
        "BW.init": "b_eh.BW.init",
        "BW.medi": "b_eh.BW.medi",
        "BW.fina": "b_eh.BW.fina",
        "BL.init": "b_l.BL.init",
        "BL.medi": "b_l.BL.medi",
        "PA.isol": "p_a.PA.isol",
        "PA.init": "p_a.PA.init",
        "PA.medi": "p_a.PA.medi",
        "PA.fina": "p_a.PA.fina",
        "PI.isol": "p_i.PI.isol",
        "PI.init": "p_i.PI.init",
        "PI.medi": "p_i.PI.medi",
        "PI.fina": "p_i.PI.fina",
        "PO.isol": "p_o.PO.isol",
        "PO.init": "p_o.PO.init",
        "PO.medi": "p_o.PO.medi",
        "PO.fina": "p_o.PO.fina",
        "PUe.isol": "p_oe.PUe.isol",
        "POI.init": "p_oe.POI.init",
        "POI.medi": "p_oe.POI.medi",
        "PUe.fina": "p_oe.PUe.fina",
        "PW.isol": "p_eh.PW.isol",
        "PW.init": "p_eh.PW.init",
        "PW.medi": "p_eh.PW.medi",
        "PW.fina": "p_eh.PW.fina",
        "GA.isol": "h_e.GA.isol",
        "GA.init": "h_e.GA.init",
        "GA.medi": "h_e.GA.medi",
        "GA.fina": "h_e.GA.fina",
        "GxA.isol": "h_e.GxA.isol",
        "GxA.init": "h_e.GxA.init",
        "GxA.medi": "h_e.GxA.medi",
        "GxA.fina": "h_e.GxA.fina",
        "GI.isol": "h_i.GI.isol",
        "GI.init": "h_i.GI.init",
        "GI.medi": "h_i.GI.medi",
        "GI.fina": "h_i.GI.fina",
        "GxI.isol": "h_i.GxI.isol",
        "GxI.init": "h_i.GxI.init",
        "GxI.medi": "h_i.GxI.medi",
        "GxI.fina": "h_i.GxI.fina",
        "GUe.isol": "h_oe.GUe.isol",
        "GO.isol": "h_oe.GO.isol",
        "GOI.init": "h_oe.GOI.init",
        "GO.init": "h_oe.GO.init",
        "GO.medi": "h_oe.GO.medi",
        "GOI.medi": "h_oe.GOI.medi",
        "GO.fina": "h_oe.GO.fina",
        "GUe.fina": "h_oe.GUe.fina",
        "GxUe.isol": "h_oe.GxUe.isol",
        "GxO.isol": "h_oe.GxO.isol",
        "GxOI.init": "h_oe.GxOI.init",
        "GxO.init": "h_oe.GxO.init",
        "GxO.medi": "h_oe.GxO.medi",
        "GxOI.medi": "h_oe.GxOI.medi",
        "GxO.fina": "h_oe.GxO.fina",
        "GxUe.fina": "h_oe.GxUe.fina",
        "GW.isol": "h_eh.GW.isol",
        "GW.init": "h_eh.GW.init",
        "GW.medi": "h_eh.GW.medi",
        "GW.fina": "h_eh.GW.fina",
        "GxW.isol": "h_eh.GxW.isol",
        "GxW.init": "h_eh.GxW.init",
        "GxW.medi": "h_eh.GxW.medi",
        "GxW.fina": "h_eh.GxW.fina",
        "GL.medi": "g_l.GL.medi",
        "MM.medi": "m_m.MM.medi",
        "ML.medi": "m_l.ML.medi",
        "LL.medi": "l_l.LL.medi",
        "FA.isol": "f_a.FA.isol",
        "FA.init": "f_a.FA.init",
        "FA.medi": "f_a.FA.medi",
        "FA.fina": "f_a.FA.fina",
        "FI.isol": "f_i.FI.isol",
        "FI.init": "f_i.FI.init",
        "FI.medi": "f_i.FI.medi",
        "FI.fina": "f_i.FI.fina",
        "FO.isol": "f_o.FO.isol",
        "FO.init": "f_o.FO.init",
        "FO.medi": "f_o.FO.medi",
        "FO.fina": "f_o.FO.fina",
        "FUe.isol": "f_oe.FUe.isol",
        "FOI.init": "f_oe.FOI.init",
        "FOI.medi": "f_oe.FOI.medi",
        "FUe.fina": "f_oe.FUe.fina",
        "FW.isol": "f_eh.FW.isol",
        "FW.init": "f_eh.FW.init",
        "FW.medi": "f_eh.FW.medi",
        "FW.fina": "f_eh.FW.fina",
        "K2A.isol": "k2_a.K2A.isol",
        "K2A.init": "k2_a.K2A.init",
        "K2A.medi": "k2_a.K2A.medi",
        "K2A.fina": "k2_a.K2A.fina",
        "K2I.isol": "k2_i.K2I.isol",
        "K2I.init": "k2_i.K2I.init",
        "K2I.medi": "k2_i.K2I.medi",
        "K2I.fina": "k2_i.K2I.fina",
        "K2O.isol": "k2_o.K2O.isol",
        "K2O.init": "k2_o.K2O.init",
        "K2O.medi": "k2_o.K2O.medi",
        "K2O.fina": "k2_o.K2O.fina",
        "K2Ue.isol": "k2_oe.K2Ue.isol",
        "K2OI.init": "k2_oe.K2OI.init",
        "K2OI.medi": "k2_oe.K2OI.medi",
        "K2Ue.fina": "k2_oe.K2Ue.fina",
        "K2W.isol": "k2_eh.K2W.isol",
        "K2W.init": "k2_eh.K2W.init",
        "K2W.medi": "k2_eh.K2W.medi",
        "K2W.fina": "k2_eh.K2W.fina",
        "KA.isol": "k_a.KA.isol",
        "KA.init": "k_a.KA.init",
        "KA.medi": "k_a.KA.medi",
        "KA.fina": "k_a.KA.fina",
        "KI.isol": "k_i.KI.isol",
        "KI.init": "k_i.KI.init",
        "KI.medi": "k_i.KI.medi",
        "KI.fina": "k_i.KI.fina",
        "KO.isol": "k_o.KO.isol",
        "KO.init": "k_o.KO.init",
        "KO.medi": "k_o.KO.medi",
        "KO.fina": "k_o.KO.fina",
        "KUe.isol": "k_oe.KUe.isol",
        "KOI.init": "k_oe.KOI.init",
        "KOI.medi": "k_oe.KOI.medi",
        "KUe.fina": "k_oe.KUe.fina",
        "KW.isol": "k_eh.KW.isol",
        "KW.init": "k_eh.KW.init",
        "KW.medi": "k_eh.KW.medi",
        "KW.fina": "k_eh.KW.fina"
    }
    yaml_mapping.update({x: k for k, v in yaml_mapping.items() if (x := translation.get(v))})
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
            # These 10 glyphs are used by EAC, not used by Baiti
            "glyph2135": ".notdef",  # oe.AU.isol
            "glyph2188": ".notdef",  # n.A.isol
            "glyph2191": ".notdef",  # sh.S.isol
            "glyph2192": ".notdef",  # sh.S.init
            "glyph2193": ".notdef",  # sh.S.medi
            "glyph2189": ".notdef",  # d.T.isol
            "glyph693": ".notdef",  # j.I2.isol
            "glyph2190": ".notdef",  # y.I.isol
            "glyph702": ".notdef",  # y.II.medi
            "glyph1827": ".notdef",  # w.O.medi
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
        output_path=baiti_dir / "res" / "Baiti-Regular.otf",
    )


if __name__ == "__main__":
    main()
