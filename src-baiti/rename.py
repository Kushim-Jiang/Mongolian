from collections.abc import Mapping

from ufoLib2 import Font
import yaml


def rename_glyphs(font: Font, name_mapping: Mapping[str, str]):
    for glyph in font:
        for component in glyph.components:
            if new_name := name_mapping.get(component.baseGlyph):
                component.baseGlyph = new_name

    for old_name, new_name in name_mapping.items():
        font.renameGlyph(old_name, new_name)


def main():
    with open("src-baiti/MongolianBaiti.yaml") as f:
        docs = yaml.load_all(f, Loader=yaml.FullLoader)

        for doc in docs:
            for k, v in doc.items():
                print(k, "->", v)


if __name__ == '__main__':
    main()