# easy-sphinx

[Autodoc](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) for [material-for-mkdocs](https://squidfunk.github.io/mkdocs-material/).

> This project is a fork of [keras-autodoc](https://github.com/keras-team/keras-autodoc), with updates made for Sphinx >= 4.0.

easy-sphinx will fetch the docstrings from the functions you wish to document and will insert them in the markdown files.

### Install

First, create a conda or virtual environment, activate it, and run:

```bash
pip install git+https://github.com/JustinGoheen/material-sphinx.git
```

### Example

> see instructions for [creating your site](https://squidfunk.github.io/mkdocs-material/creating-your-site/) provided by material-for-mkdocs to create the proper directory structure.

Let's suppose that you have a project with a `docs` directory:

```
/project-root
    |--/source_code
        __init__.py
        main.py
    |--./docs
        autogen.py
    mkdocs.yml
    setup.py
```

The API is quite simple:

```python
# content of docs/autogen.py

from easy_sphinx import DocumentationGenerator


pages = {'layers/core.md': ['keras.layers.Dense', 'keras.layers.Flatten'],
         'callbacks.md': ['keras.callbacks.TensorBoard']}

doc_generator = DocumentationGenerator(pages)
doc_generator.generate('./sources')
```

```yaml
# content of docs/mkdocs.yml

site_name: My_site
docs_dir: docs/sources
site_description: 'My pretty site.'

nav:
    - Core: layers/core.md
    - Callbacks:
      - Some callbacks: callbacks.md
```

Then you just have to run:

```bash
python docs/autogen.py
mkdocs serve
```

and you'll be able to see your website at [localhost:8000/callbacks](http://localhost:8000/callbacks/).

### Docstring format:

The docstrings used should use the Google docstring style, found in the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) with markdown, or just plain markdown.


### Deploying your site

See the instructions for [deploying your site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/) provided by material-for-mkdocs.
