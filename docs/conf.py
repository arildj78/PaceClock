# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Svømmeklokke2'
copyright = '2026, Arild M Johannessen'
author = 'Arild M Johannessen'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'myst_parser',  # For Markdown support
]

# Source file parsers
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Read the Docs theme
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# Use a global table of contents in the sidebar so navigation stays consistent
# across pages instead of changing to the current section only.
html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ]
}

# Logo and favicon
# html_logo = '../bsk.png'
# html_favicon = '../bsk_sirkel.png'

html_title = 'Svømmeklokke2 Documentation'
html_short_title = 'Swim Clock'

# Add any paths that contain custom static files (such as style sheets)
html_css_files = []

# GitHub integration
html_context = {
    'display_github': True,
    'github_user': 'arildj78',  # Update with your GitHub username
    'github_repo': 'PaceClock',  # Update with your repo name
    'github_version': 'main',
    'conf_py_path': '/docs/',
}
