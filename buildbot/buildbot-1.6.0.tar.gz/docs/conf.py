# -*- coding: utf-8 -*-
#
# Buildbot documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 10 15:13:31 2010.
#
# This file is exec()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pkg_resources
import sys
import textwrap

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

try:
    from buildbot.util.raml import RamlSpec
except ImportError:
    sys.path.insert(2, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir))
    from buildbot.util.raml import RamlSpec

# -- General configuration -----------------------------------------------
try:
    import sphinxcontrib.blockdiag
    assert sphinxcontrib.blockdiag
except ImportError:
    raise RuntimeError("sphinxcontrib.blockdiag is not installed. "
                       "Please install documentation dependencies with `pip install buildbot[docs]`")

try:
    pkg_resources.require('docutils>=0.8')
except pkg_resources.ResolutionError:
    raise RuntimeError("docutils is not installed or has incompatible version. "
                       "Please install documentation dependencies with `pip install buildbot[docs]`")
# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'bbdocs.ext',
    'bbdocs.highlighterrors',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.jinja',
]
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Buildbot'
copyright = u'Buildbot Team Members'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

if 'VERSION' in os.environ:
    version = os.environ['VERSION']
else:
    gl = {'__file__': '../buildbot/__init__.py'}
    with open('../buildbot/__init__.py') as f:
        exec(f.read(), gl)
    version = gl['version']

# The full version, including alpha/beta/rc tags.
release = version

# blocksiag/seqdiag
blockdiag_html_image_format = 'svg'
blocdiag_transparency = True

# add a loud note for anyone looking at the latest docs
if release == 'latest':
    rst_prolog = textwrap.dedent("""\
    .. caution:: This page documents the latest, unreleased version of
        Buildbot.  For documentation for released versions, see
        http://docs.buildbot.net/current/.

    """)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'release-notes/*.rst']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

intersphinx_mapping = {
    'python': ('https://python.readthedocs.io/en/latest/', None),
    'sqlalchemy': ('https://sqlalchemy.readthedocs.io/en/latest/', None),
}

extlinks = {
    'pull': ('https://github.com/buildbot/buildbot/pull/%s', 'pull request '),
    'issue': ('https://github.com/buildbot/buildbot/issues/%s', 'issue # '),
    # deprecated. Use issue instead, and point to Github
    'bug': ('http://trac.buildbot.net/ticket/%s', 'bug #'),
    # Renders as link with whole url, e.g.
    #   :src-link:`master`
    # renders as
    #   "https://github.com/buildbot/buildbot/blob/master/master".
    # Explicit title can be used for customizing how link looks like:
    #   :src-link:`master's directory <master>`
    'src-link': ('https://github.com/buildbot/buildbot/tree/master/%s', None),
    # "pretty" reference that looks like relative path in Buildbot source tree
    # by default.
    'src': ('https://github.com/buildbot/buildbot/tree/master/%s', ''),
    'contrib-src': ('https://github.com/buildbot/buildbot-contrib/tree/master/%s', ''),
}

# Sphinx' link checker.
linkcheck_ignore = [
    # Local URLs:
    r'^http://localhost.*',
    # Available only to logged-in users:
    r'^https://github\.com/settings/applications$',
    # Sites which uses SSL that Python 2 can't handle:
    r'^https://opensource\.org/licenses/gpl-2.0\.php$',
    r'^https://docs\.docker\.com/engine/installation/$',
    # Looks like server doesn't like user agent:
    r'^https://www\.microsoft\.com/en-us/download/details\.aspx\?id=17657$',
    # Example domain.
    r'^https?://(.+\.)?example\.org',
    # Anchor check fails on rendered user files on GitHub, since GitHub uses
    # custom prefix for anchors in user generated content.
    r'https://github\.com/buildbot/guanlecoja-ui/tree/master#changelog',
    r'http://mesosphere.github.io/marathon/docs/rest-api.html#post-v2-apps',
]
linkcheck_timeout = 10
linkcheck_retries = 3
linkcheck_workers = 20

# -- Options for HTML output ---------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'qtile'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {'stickysidebar': 'true'}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [
    '_themes'
]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join('_images', 'full_logo.png')

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large or a png.
html_favicon = os.path.join('_static', 'icon.png')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['searchbox.html', 'localtoc.html', 'relations.html', 'sourcelink.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

html_use_index = True
html_use_modindex = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Buildbotdoc'


# -- Options for LaTeX output --------------------------------------------

latex_elements = {}
# The paper size ('letter' or 'a4').
latex_elements['papersize'] = 'a4'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '11pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'Buildbot.tex', u'Buildbot Documentation',
     u'Brian Warner', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = os.path.join('_images', 'header-text-transparent.png')

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# Three possible values for this option (see sphinx config manual) are:
# 1. 'no' - do not display URLs (default)
# 2. 'footnote' - display URLs in footnotes
# 3. 'inline' - display URLs inline in parentheses
latex_show_urls = 'inline'

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'buildbot', u'Buildbot Documentation',
     [u'Brian Warner'], 1)
]

jinja_contexts = {
    "data_api": {'raml': RamlSpec()}
}

# Spell checker.
try:
    import enchant  # noqa # pylint: disable=unused-import
except ImportError as ex:
    print("enchant module import failed:\n"
          "{0}\n"
          "Spell checking disabled.".format(ex),
          file=sys.stderr)

else:
    extensions.append('sphinxcontrib.spelling')
    spelling_show_suggestions = True
