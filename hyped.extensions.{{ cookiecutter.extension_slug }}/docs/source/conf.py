# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Include package path
import os
import sys

sys.path.insert(0, os.path.abspath("../../src/hyped/extensions/"))

# import all modules
import {{ cookiecutter.extension_slug }}  # noqa: E402

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.pypi_extension_name }}"
copyright = "2024, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
version = {{ cookiecutter.extension_slug }}.__version__
release = {{ cookiecutter.extension_slug }}.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = []

# Add intersphinx mapping for external projects
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    # TODO: link to public hyped documentation
    "hyped": (os.path.abspath("../../../../hyped/docs/build/html"), None),
}

# syntax highlighting
pygments_style = "monokai"
pygments_dark_style = "native"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]