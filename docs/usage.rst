.. _ref-usage:

=====
Usage
=====

Describes how to use Pipeline when it is installed and configured.


Template tags
=============

Pipeline includes two template tags: ``stylesheet`` and ``javascript``, in a
template library called ``pipeline``.

They are used to output the ``<link>`` and ``<script>``-tags for the specified
CSS/JavaScript-groups (as specified in the settings). The first argument must
be the name of the CSS/JavaScript group.

When :djangosetting:`DEBUG` is set to ``True`` the use of these template tags
will result in a separate tag for each resource in a given group (i.e., the
combined, compressed files will not be used), in order to make local debugging
easy. When ``settings.DEBUG`` is set to ``False`` the opposite is true. You can
override the default behavior by setting :confval:`PIPELINE_ENABLED` manually.
When set to ``True`` or ``False`` this enables or disables, respectively, the
usage of the combined, compressed file for each resource group. This can be
useful, if you encounter errors in your compressed code that don't occur in
your uncompressed code and you want to debug them locally.

If you need to change the output of the HTML-tags generated from the
templatetags, this can be done by overriding the templates
:file:`pipeline/css.html` and :file:`pipeline/js.html`.


Example
-------

If you have specified the CSS-groups “colors” and “stats” and a JavaScript-group
with the name “scripts”, you would use the following code to output them all:

.. code-block:: django

   {% load pipeline %}

   {% stylesheet "colors" %}
   {% stylesheet "stats" %}
   {% javascript "scripts" %}


Development performance
-----------------------

When :confval:`PIPELINE_ENABLED` is ``False`` and
:confval:`PIPELINE_COLLECTOR_ENABLED` is ``True``, the template tags collect
your static files before they render. Pipeline only does this once per
request, but it needs the ``request`` variable in the template context to
tell requests apart. Without it, Pipeline collects the files again for every
template tag on the page, which can make pages much slower to load.

To avoid this, make sure the ``request`` context processor is turned on.
Django's default project template already includes it:

.. code-block:: python
   :caption: settings.py

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            ...
            "OPTIONS": {
                "context_processors": [
                    ...
                    "django.template.context_processors.request",
                ],
            },
        },
    ]


Form Media
==========

Django forms and widgets can specify individual CSS or JavaScript files to
include on a page by defining a ``Form.Media`` class with ``css`` and ``js``
attributes.

Pipeline builds upon this by allowing packages to be listed in
``css_packages`` and ``js_packages``. This is equivalent to manually including
these packages in a page's template using the template tags.

To use these, just have your form or widget's ``Media`` class inherit from
:py:class:`~pipeline.forms.PipelineFormMedia` and define ``css_packages`` and
``js_packages``. You can also continue to reference individual CSS/JavaScript
files using the original ``css``/``js`` attributes, if needed.

Note that unlike the template tags, you cannot customize the HTML for
referencing these files. The :file:`pipeline/css.html` and
:file:`pipeline/js.html` files will not be used. Django takes care of
generating the HTML for form and widget media.


Example
-------

.. code-block:: python
   :caption: app/forms.py

    from django import forms
    from pipeline.forms import PipelineFormMedia

    class MyForm(forms.Form):
        ...

        class Media(PipelineFormMedia):
            css_packages = {
                "all": ("my-styles",)
            }
            js_packages = ("my-scripts",)
            js = ("https://cdn.example.com/some-script.js",)


Collecting static media
=======================

Pipeline provides storage backends for Django's ``staticfiles`` app. These will
compile and compress your static media when running :command:`manage.py
collectstatic`.

This can be set as the storage backend for staticfiles:

.. code-block:: python
   :caption: settings.py

    STORAGES = {
        ...
        "staticfiles": {"BACKEND": "pipeline.storage.PipelineStorage"},
    }

Or, if you would like to use filenames that include hashes for cache-busting:

.. code-block:: python
   :caption: settings.py

    STORAGES = {
        ...
        "staticfiles": {"BACKEND": "pipeline.storage.PipelineManifestStorage"},
    }

See :doc:`storages` for more detail.


Middleware
==========

To enable HTML compression add
:py:class:`pipeline.middleware.MinifyHTMLMiddleware` to your
:djangosetting:`MIDDLEWARE` setting.

Ensure that it comes after any middleware which modifies your HTML, like
``GZipMiddleware``:

.. code-block:: python
   :caption: settings.py

    MIDDLEWARE = (
        "django.middleware.gzip.GZipMiddleware",
        "pipeline.middleware.MinifyHTMLMiddleware",
    )


Jinja
=====

Pipeline also includes Jinja2 support and is used almost identically to the
Django Template tags implementation. You just need to pass
:py:class:`pipeline.jinja2.PipelineExtension` to your Jinja2 environment:

.. code-block:: python
   :caption: settings.py

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.jinja2.Jinja2",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "environment": "myproject.jinja2.environment",
                "extensions": ["pipeline.jinja2.PipelineExtension"],
            }
        },
    ]


Templates
---------

Unlike the Django template tag implementation the Jinja2 implementation uses
different templates, so if you wish to override them please override
:file:`pipeline/css.jinja` and :file:`pipeline/js.jinja`.
