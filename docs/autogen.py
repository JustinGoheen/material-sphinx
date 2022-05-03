import pathlib
import shutil

import material_sphinx


PAGES = {
    'documentation_generator.md': [
        'material_sphinx.DocumentationGenerator',
        'material_sphinx.DocumentationGenerator.generate',
    ],
    'automatic_gathering.md': [
        'material_sphinx.get_functions',
        'material_sphinx.get_classes',
        'material_sphinx.get_methods',
    ]
}


material_sphinx_dir = pathlib.Path(__file__).resolve().parents[1]


def generate(dest_dir):
    doc_generator = material_sphinx.DocumentationGenerator(
        PAGES,
        'https://github.com/JustinGoheenAI/material-sphinx/blob/main',
    )
    doc_generator.generate(dest_dir)
    shutil.copyfile(material_sphinx_dir / 'README.md', dest_dir / 'index.md')


if __name__ == '__main__':
    generate(material_sphinx_dir / 'docs' / 'sources')
