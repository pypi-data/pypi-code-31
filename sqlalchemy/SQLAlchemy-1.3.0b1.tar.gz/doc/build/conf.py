# -*- coding: utf-8 -*-
#
# SQLAlchemy documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 26 19:50:10 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../lib'))
sys.path.insert(0, os.path.abspath('../..')) # examples
sys.path.insert(0, os.path.abspath('.'))

import sqlalchemy


# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.6.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
            'sphinx.ext.autodoc',
            'zzzeeksphinx',
            'changelog',
            'sphinx_paramlinks',
            ]

# Add any paths that contain templates here, relative to this directory.
# not sure why abspath() is needed here, some users
# have reported this.
templates_path = [os.path.abspath('templates')]

nitpicky = True

# The suffix of source filenames.
source_suffix = '.rst'


# section names used by the changelog extension.
changelog_sections = ["general", "orm", "orm declarative", "orm querying", \
                "orm configuration", "engine", "sql", \
                "schema", \
                "postgresql", "mysql", "sqlite", "mssql", \
                "oracle", "firebird"]
# tags to sort on inside of sections
changelog_inner_tag_sort = ["feature", "changed", "removed", "bug", "moved"]

# how to render changelog links
changelog_render_ticket = "http://www.sqlalchemy.org/trac/ticket/%s"

changelog_render_pullreq = {
    "bitbucket": "https://bitbucket.org/zzzeek/sqlalchemy/pull-request/%s",
    "default": "https://bitbucket.org/zzzeek/sqlalchemy/pull-request/%s",
    "github": "https://github.com/zzzeek/sqlalchemy/pull/%s",
}

changelog_render_changeset = "http://www.sqlalchemy.org/trac/changeset/%s"

exclude_patterns = [
    'build',
    '**/unreleased*/*',
]

autodocmods_convert_modname = {
    "sqlalchemy.sql.sqltypes": "sqlalchemy.types",
    "sqlalchemy.sql.type_api": "sqlalchemy.types",
    "sqlalchemy.sql.schema": "sqlalchemy.schema",
    "sqlalchemy.sql.elements": "sqlalchemy.sql.expression",
    "sqlalchemy.sql.selectable": "sqlalchemy.sql.expression",
    "sqlalchemy.sql.dml": "sqlalchemy.sql.expression",
    "sqlalchemy.sql.ddl": "sqlalchemy.schema",
    "sqlalchemy.sql.base": "sqlalchemy.sql.expression",
    "sqlalchemy.engine.base": "sqlalchemy.engine",
    "sqlalchemy.engine.result": "sqlalchemy.engine",
}

autodocmods_convert_modname_w_class = {
    ("sqlalchemy.engine.interfaces", "Connectable"): "sqlalchemy.engine",
    ("sqlalchemy.sql.base", "DialectKWArgs"): "sqlalchemy.sql.base",
}

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'SQLAlchemy'
copyright = u'2007-2018, the SQLAlchemy authors and contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.3"
# The full version, including alpha/beta/rc tags.
release = "1.3.0b1"

release_date = "November 16, 2018"

site_base = os.environ.get("RTD_SITE_BASE", "http://www.sqlalchemy.org")
site_adapter_template = "docs_adapter.mako"
site_adapter_py = "docs_adapter.py"

# arbitrary number recognized by builders.py, incrementing this
# will force a rebuild
build_number = "3"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# have the "gettext" build generate .pot for each individual
# .rst
gettext_compact = False

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'zzzeeksphinx'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "%s %s Documentation" % (project, version)

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%m/%d/%Y %H:%M:%S'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
    "notfound": "notfound.html"
}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True
html_copy_source = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'SQLAlchemydoc'

#autoclass_content = 'both'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('contents', 'sqlalchemy_%s.tex' % release.replace('.', '_'), 'SQLAlchemy Documentation',
   'Mike Bayer', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
# sets TOC depth to 2.
latex_preamble = '\setcounter{tocdepth}{3}'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

#latex_elements = {
#    'papersize': 'letterpaper',
#    'pointsize': '10pt',
#}

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'sqlalchemy', u'SQLAlchemy Documentation',
     [u'SQLAlchemy authors'], 1)
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'SQLAlchemy'
epub_author = u'SQLAlchemy authors'
epub_publisher = u'SQLAlchemy authors'
epub_copyright = u'2007-2015, SQLAlchemy authors'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True


