from pathlib import Path
from fontmake.font_project import FontProject
from ufoLib2 import Font

from rename import build_mapping_from_yaml, rename_glyphs

repository_dir = Path(__file__).parent.parent
baiti_dir = repository_dir / "src-baiti"
res_dir = baiti_dir / "res"
temp_dir = baiti_dir / "temp"
otl_dir = baiti_dir / "hudum-feature"


def main():
    temp_dir.mkdir(exist_ok=True)

    ufo = Font.open(baiti_dir / "161Source005-cubic.ufo")
    # ufo.info.unitsPerEm = ufo.info.unitsPerEm / 1.25
    ufo.info.familyName = "Draft Baiti"
    ufo.info.postscriptFullName = "Draft Baiti Regular"
    ufo.info.postscriptFontName = "DraftBaiti-Regular"
    ufo.info.styleMapFamilyName = "Draft Baiti Regular"

    # rename glyph
    yaml_dir = baiti_dir / "MongolianBaiti.yaml"
    yaml_mapping = build_mapping_from_yaml(yaml_dir)

    translation = {
        "b_a.BA.isol": "BA.isol",
        "b_a.BA.init": "BA.init",
        "b_a.BA.medi": "BA.medi",
        "b_a.BA.fina": "BA.fina",
        "b_i.BI.isol": "BI.isol",
        "b_i.BI.init": "BI.init",
        "b_i.BI.medi": "BI.medi",
        "b_i.BI.fina": "BI.fina",
        "b_o.BO.isol": "BO.isol",
        "b_o.BO.init": "BO.init",
        "b_o.BO.medi": "BO.medi",
        "b_o.BO.fina": "BO.fina",
        "b_oe.BUe.isol": "BUe.isol",
        "b_oe.BOI.init": "BOI.init",
        "b_oe.BOI.medi": "BOI.medi",
        "b_oe.BUe.fina": "BUe.fina",
        "b_eh.BW.isol": "BW.isol",
        "b_eh.BW.init": "BW.init",
        "b_eh.BW.medi": "BW.medi",
        "b_eh.BW.fina": "BW.fina",
        "b_l.BL.init": "BL.init",
        "b_l.BL.medi": "BL.medi",
        "p_a.PA.isol": "PA.isol",
        "p_a.PA.init": "PA.init",
        "p_a.PA.medi": "PA.medi",
        "p_a.PA.fina": "PA.fina",
        "p_i.PI.isol": "PI.isol",
        "p_i.PI.init": "PI.init",
        "p_i.PI.medi": "PI.medi",
        "p_i.PI.fina": "PI.fina",
        "p_o.PO.isol": "PO.isol",
        "p_o.PO.init": "PO.init",
        "p_o.PO.medi": "PO.medi",
        "p_o.PO.fina": "PO.fina",
        "p_oe.PUe.isol": "PUe.isol",
        "p_oe.POI.init": "POI.init",
        "p_oe.POI.medi": "POI.medi",
        "p_oe.PUe.fina": "PUe.fina",
        "p_eh.PW.isol": "PW.isol",
        "p_eh.PW.init": "PW.init",
        "p_eh.PW.medi": "PW.medi",
        "p_eh.PW.fina": "PW.fina",
        "h_e.GA.isol": "GA.isol",
        "h_e.GA.init": "GA.init",
        "h_e.GA.medi": "GA.medi",
        "h_e.GA.fina": "GA.fina",
        "h_e.GxA.isol": "GxA.isol",
        "h_e.GxA.init": "GxA.init",
        "h_e.GxA.medi": "GxA.medi",
        "h_e.GxA.fina": "GxA.fina",
        "h_i.GI.isol": "GI.isol",
        "h_i.GI.init": "GI.init",
        "h_i.GI.medi": "GI.medi",
        "h_i.GI.fina": "GI.fina",
        "h_i.GxI.isol": "GxI.isol",
        "h_i.GxI.init": "GxI.init",
        "h_i.GxI.medi": "GxI.medi",
        "h_i.GxI.fina": "GxI.fina",
        "h_oe.GUe.isol": "GUe.isol",
        "h_oe.GO.isol": "GO.isol",
        "h_oe.GOI.init": "GOI.init",
        "h_oe.GO.init": "GO.init",
        "h_oe.GO.medi": "GO.medi",
        "h_oe.GOI.medi": "GOI.medi",
        "h_oe.GO.fina": "GO.fina",
        "h_oe.GUe.fina": "GUe.fina",
        "h_oe.GxUe.isol": "GxUe.isol",
        "h_oe.GxO.isol": "GxO.isol",
        "h_oe.GxOI.init": "GxOI.init",
        "h_oe.GxO.init": "GxO.init",
        "h_oe.GxO.medi": "GxO.medi",
        "h_oe.GxOI.medi": "GxOI.medi",
        "h_oe.GxO.fina": "GxO.fina",
        "h_oe.GxUe.fina": "GxUe.fina",
        "h_eh.GW.isol": "GW.isol",
        "h_eh.GW.init": "GW.init",
        "h_eh.GW.medi": "GW.medi",
        "h_eh.GW.fina": "GW.fina",
        "h_eh.GxW.isol": "GxW.isol",
        "h_eh.GxW.init": "GxW.init",
        "h_eh.GxW.medi": "GxW.medi",
        "h_eh.GxW.fina": "GxW.fina",
        "g_l.GL.medi": "GL.medi",
        "m_m.MM.medi": "MM.medi",
        "m_l.ML.medi": "ML.medi",
        "l_l.LL.medi": "LL.medi",
        "f_a.FA.isol": "FA.isol",
        "f_a.FA.init": "FA.init",
        "f_a.FA.medi": "FA.medi",
        "f_a.FA.fina": "FA.fina",
        "f_i.FI.isol": "FI.isol",
        "f_i.FI.init": "FI.init",
        "f_i.FI.medi": "FI.medi",
        "f_i.FI.fina": "FI.fina",
        "f_o.FO.isol": "FO.isol",
        "f_o.FO.init": "FO.init",
        "f_o.FO.medi": "FO.medi",
        "f_o.FO.fina": "FO.fina",
        "f_oe.FUe.isol": "FUe.isol",
        "f_oe.FOI.init": "FOI.init",
        "f_oe.FOI.medi": "FOI.medi",
        "f_oe.FUe.fina": "FUe.fina",
        "f_eh.FW.isol": "FW.isol",
        "f_eh.FW.init": "FW.init",
        "f_eh.FW.medi": "FW.medi",
        "f_eh.FW.fina": "FW.fina",
        "k2_a.K2A.isol": "K2A.isol",
        "k2_a.K2A.init": "K2A.init",
        "k2_a.K2A.medi": "K2A.medi",
        "k2_a.K2A.fina": "K2A.fina",
        "k2_i.K2I.isol": "K2I.isol",
        "k2_i.K2I.init": "K2I.init",
        "k2_i.K2I.medi": "K2I.medi",
        "k2_i.K2I.fina": "K2I.fina",
        "k2_o.K2O.isol": "K2O.isol",
        "k2_o.K2O.init": "K2O.init",
        "k2_o.K2O.medi": "K2O.medi",
        "k2_o.K2O.fina": "K2O.fina",
        "k2_oe.K2Ue.isol": "K2Ue.isol",
        "k2_oe.K2OI.init": "K2OI.init",
        "k2_oe.K2OI.medi": "K2OI.medi",
        "k2_oe.K2Ue.fina": "K2Ue.fina",
        "k2_eh.K2W.isol": "K2W.isol",
        "k2_eh.K2W.init": "K2W.init",
        "k2_eh.K2W.medi": "K2W.medi",
        "k2_eh.K2W.fina": "K2W.fina",
        "k_a.KA.isol": "KA.isol",
        "k_a.KA.init": "KA.init",
        "k_a.KA.medi": "KA.medi",
        "k_a.KA.fina": "KA.fina",
        "k_i.KI.isol": "KI.isol",
        "k_i.KI.init": "KI.init",
        "k_i.KI.medi": "KI.medi",
        "k_i.KI.fina": "KI.fina",
        "k_o.KO.isol": "KO.isol",
        "k_o.KO.init": "KO.init",
        "k_o.KO.medi": "KO.medi",
        "k_o.KO.fina": "KO.fina",
        "k_oe.KUe.isol": "KUe.isol",
        "k_oe.KOI.init": "KOI.init",
        "k_oe.KOI.medi": "KOI.medi",
        "k_oe.KUe.fina": "KUe.fina",
        "k_eh.KW.isol": "KW.isol",
        "k_eh.KW.init": "KW.init",
        "k_eh.KW.medi": "KW.medi",
        "k_eh.KW.fina": "KW.fina",
    }

    yaml_mapping.update({baiti: eac for baiti, utn in yaml_mapping.items() if (eac := translation.get(utn))})
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
            # These glyphs are not used by Baiti
            "oe.AU.isol": ".notdef",
            "n.A.init._isol": ".notdef",
            "sh.S.init._isol": ".notdef",
            "sh.S.init": ".notdef",
            "sh.S.medi": ".notdef",
            "d.T.init._isol": ".notdef",
            "y.I.init._isol": ".notdef",
            "y.II.medi": ".notdef",
            "w.O.medi": ".notdef",
            "nirugu.effective": "nirugu",
    }.items():
        ufo[constructed] = ufo[origin].copy()

    # TODO, FIXME
    for name in [
            "zwnj", "zwj", "mvs.effective", "nnbsp.effective", "fvs1.effective", "fvs2.effective", "fvs3.effective", "fvs4.effective", "nil", "_nil", "_helper"
    ]:
        ufo.newGlyph(name)
        if name == "mvs.effective":
            ufo[name].width = 300
        if name == "nnbsp.effective":
            ufo[name].width = 500
        if name == "_mvs":
            ufo[name].width = 300
        if name == "_nnbsp":
            ufo[name].width = 500

    # feature
    for path in otl_dir.iterdir():
        if path.suffix == ".fea":
            (temp_dir / path.name).write_text(path.read_text())

    # ufo.features.text = "include(main.fea);\n include(lookups-vertical.fea);\n"
    ufo.features.text = "include(main.fea);\n"

    path = temp_dir / "font.ufo"
    ufo.save(path, overwrite=True)  # fontmake reads from

    project = FontProject()
    project.run_from_ufos(
        str(path),
        output=["otf"],
        remove_overlaps=True,
        output_path=baiti_dir / "res" / "Baiti-Regular.otf",
    )


if __name__ == "__main__":
    main()
