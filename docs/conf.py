from datetime import datetime

from sphinx.application import Sphinx

from pipeline import __version__ as pipeline_version

source_suffix = ".rst"
master_doc = "index"
templates_path = ["_templates"]
exclude_patterns = ["_build"]

# General information about the project.
project = "django-pipeline"
current_year = datetime.now().year
copyright = f"2011-{current_year}, django-pipeline contributors"

# The full version, including alpha/beta/rc tags.
release = pipeline_version
# The short X.Y version.
version = ".".join(release.split(".")[:2])

# Enabled extensions.
extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

# sphinx-autoapi configuration.
autoapi_dirs = ["../pipeline"]
autoapi_root = "reference"
autoapi_add_toctree_entry = False
autoapi_member_order = "bysource"
autoapi_python_class_content = "both"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
]
autodoc_typehints = "description"

# Internal modules to leave out of the reference. They are still parsed so
# that imports from them resolve.
autoapi_skip_modules = {
    "pipeline.collector",
    "pipeline.conf",
    "pipeline.glob",
    "pipeline.utils",
}


# Intersphinx configuration.
intersphinx_mapping = {
    "django": (
        "https://docs.djangoproject.com/en/stable/",
        "https://docs.djangoproject.com/en/stable/_objects/",
    ),
    "jinja": (
        "https://jinja.palletsprojects.com/en/stable/",
        None,
    ),
    "python": (
        "https://docs.python.org/3",
        None,
    ),
}

# Base classes that the code reference links to, but which Django does not
# document.
nitpick_ignore = [
    ("py:obj", "django.contrib.staticfiles.finders.AppDirectoriesFinder"),
    ("py:obj", "django.contrib.staticfiles.finders.BaseFinder"),
    ("py:obj", "django.contrib.staticfiles.finders.BaseStorageFinder"),
    ("py:obj", "django.contrib.staticfiles.finders.FileSystemFinder"),
    ("py:obj", "django.template.Node"),
]

# SourceForge blocks automated requests, so these links always look broken.
linkcheck_ignore = [
    r"https://csstidy\.sourceforge\.net/",
]

# -- Options for HTML output ---------------------------------------------------
html_theme = "shibuya"
html_theme_options = {
    "accent_color": "indigo",
}
htmlhelp_basename = "django-pipelinedoc"


# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    (
        "index",
        "django-pipeline.tex",
        "Pipeline Documentation",
        "Timothée Peignier",
        "manual",
    ),
]

# -- Options for manual page output --------------------------------------------
man_pages = [
    ("index", "django-pipeline", "Pipeline Documentation", ["Timothée Peignier"], 1)
]


def skip_internal_modules(
    app: Sphinx,
    what: str,
    name: str,
    obj: object,
    skip: bool,
    options: list[str],
) -> bool:
    if what == "module" and name in autoapi_skip_modules:
        return True

    return skip


def setup(app: Sphinx) -> None:
    app.connect("autoapi-skip-member", skip_internal_modules)

    # Django's docs define the "setting" type in their own extension. Declare
    # it here so that :djangosetting: links resolve through intersphinx. The
    # type name must stay "setting" to match Django's inventory.
    app.add_crossref_type(
        directivename="setting",
        rolename="djangosetting",
        indextemplate="pair: %s; setting",
    )
