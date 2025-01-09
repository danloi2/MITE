# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MITE 2025'
copyright = '2025, Daniel Losada'
author = 'Daniel Losada'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ["myst_parser", "sphinx_design"]
myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output



# Configuración del tema
html_theme = "sphinx_book_theme"
html_static_path = ['_static']

# Configuración del logo
html_logo = "_static/logo.png"

# Configuración de los colores
sd_custom_directives = {
    "dropdown-syntax": {
        "inherit": "dropdown",
        "argument": "Syntax",
        "options": {
            "color": "primary",
            "icon": "code",
        },
    }
}