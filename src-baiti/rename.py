from collections.abc import Mapping

from ufoLib2 import Font
import yaml


def rename_glyphs(font: Font, name_mapping: Mapping[str, str]) -> None:
    for glyph in font:
        for component in glyph.components:
            if new_name := name_mapping.get(component.baseGlyph):
                component.baseGlyph = new_name

    for old_name, new_name in name_mapping.items():
        font.renameGlyph(old_name, new_name)


def build_mapping_from_yaml(path: str) -> Mapping:
    mapping = dict()

    with open(path) as f:
        docs = yaml.load_all(f, Loader=yaml.FullLoader)

        for doc in docs:
            for k, v in doc.items():
                mapping[str(k)] = v
    return mapping


if __name__ == '__main__':
    path = "src-baiti/MongolianBaiti.yaml"
    mapping = build_mapping_from_yaml(path)