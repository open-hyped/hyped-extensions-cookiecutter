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
    "sphinx.ext.viewcode"
]

templates_path = ["_templates"]
exclude_patterns = []

# syntax highlighting
pygments_style = "monokai"
pygments_dark_style = "native"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_theme_options = {
    "canonical_url": "",
    "analytics_id": "",  # Set this to your Google Analytics tracking ID
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#007bff",
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "includehidden": True,
    "titles_only": False,
}
