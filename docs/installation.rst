.. _ref-installation:

============
Installation
============

1. Install the latest release from PyPI_:

   .. code-block:: console

       $ pip install django-pipeline


2. Add "pipeline" to your ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = (
           ...
           "pipeline",
       )

3. Use a pipeline storage for the ``staticfiles`` storage:

   .. code-block:: python

        STORAGES = {
            "default": {
                "BACKEND": "django.core.files.storage.FileSystemStorage",
            },
            "staticfiles": {
                "BACKEND": "pipeline.storage.PipelineManifestStorage",
            },
        }

   On Django 4.0 and 4.1, use the older setting instead:

   .. code-block:: python

       STATICFILES_STORAGE = "pipeline.storage.PipelineManifestStorage"

4. Add the ``PipelineFinder`` to ``STATICFILES_FINDERS``:

   .. code-block:: python

        STATICFILES_FINDERS = (
            "django.contrib.staticfiles.finders.FileSystemFinder",
            "django.contrib.staticfiles.finders.AppDirectoriesFinder",
            "pipeline.finders.PipelineFinder",
        )


.. _PyPI: https://pypi.org/project/django-pipeline/

Recommendations
===============

Pipeline's default CSS and JS compressor is Yuglify.
Yuglify wraps UglifyJS and cssmin, applying the default YUI configurations to them.
It can be downloaded from: https://github.com/yui/yuglify/.

If you do not install yuglify, make sure to disable the compressor in your settings.
