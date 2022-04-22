import pathlib
import shutil

import easy_sphinx


PAGES = {
    'documentation_generator.md': [
        'easy_sphinx.DocumentationGenerator',
        'easy_sphinx.DocumentationGenerator.generate',
    ],
    'automatic_gathering.md': [
        'easy_sphinx.get_functions',
        'easy_sphinx.get_classes',
        'easy_sphinx.get_methods',
    ]
}


easy_sphinx_dir = pathlib.Path(__file__).resolve().parents[1]


def generate(dest_dir):
    doc_generator = easy_sphinx.DocumentationGenerator(
        PAGES,
        'https://github.com/keras-team/keras-autodoc/blob/master',
    )
    doc_generator.generate(dest_dir)
    shutil.copyfile(easy_sphinx_dir / 'README.md', dest_dir / 'index.md')


if __name__ == '__main__':
    generate(easy_sphinx_dir / 'docs' / 'sources')
