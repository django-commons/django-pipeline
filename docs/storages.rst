.. _ref-storages:

================
Storage backends
================

Using with staticfiles
======================

Pipeline provides a Django storage class for the :doc:`staticfiles app
<django:howto/static-files/index>`. To use it, set the ``staticfiles`` storage
backend in :djangosetting:`STORAGES`:

.. code-block:: python
   :caption: settings.py

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "pipeline.storage.PipelineStorage",
        },
    }

On Django 4.0 and 4.1, set ``STATICFILES_STORAGE`` to the same class instead.
The examples below only show the ``staticfiles`` entry.


Additional storage backends
---------------------------

Pipeline includes several other storage backends with various behaviors:

:py:class:`pipeline.storage.PipelineManifestStorage`
    This backend behaves like Django's
    :py:class:`~django.contrib.staticfiles.storage.ManifestStaticFilesStorage`,
    adding a hash to filenames in order to provide cache-busting.

:py:class:`pipeline.storage.NonPackagingPipelineStorage`
    This backend allows you to run :command:`manage.py collectstatic` without
    packaging your assets.

:py:class:`pipeline.storage.NonPackagingPipelineManifestStorage`
    A backend that adds a hash to filenames but does not package assets.


Finders
-------

If you use staticfiles with ``DEBUG = False`` (i.e. for integration tests with
`Selenium <https://www.selenium.dev/>`_) you should install the finder that allows
staticfiles to locate your outputted assets:

.. code-block:: python
   :caption: settings.py

    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
        "pipeline.finders.PipelineFinder",
    )

If you use :py:class:`~pipeline.storage.PipelineManifestStorage`, you may also
want to use the :py:class:`~pipeline.finders.CachedFileFinder`, which allows
you to use integration tests with hashed file URLs.

If you want to exclude Pipelinable content from your collected static files,
you can also use Pipeline's :py:class:`~pipeline.finders.FileSystemFinder` and
:py:class:`~pipeline.finders.AppDirectoriesFinder`. These finders will also
exclude unwanted content like READMEs, tests and examples.

.. code-block:: python
   :caption: settings.py

    STATICFILES_FINDERS = (
        "pipeline.finders.FileSystemFinder",
        "pipeline.finders.AppDirectoriesFinder",
        "pipeline.finders.CachedFileFinder",
        "pipeline.finders.PipelineFinder",
    )

GZIP compression
================

Pipeline can also create a gzipped version of your collected static files, so
that you can avoid compressing them on the fly. To use that, create a new
storage subclass that mixes in :py:class:`~pipeline.storage.GZIPMixin`:

.. code-block:: python
   :caption: app/storage.py

    from pipeline.storage import GZIPMixin, PipelineManifestStorage

    class GZIPManifestStorage(GZIPMixin, PipelineManifestStorage):
        pass

Then set the storage backend in your :file:`settings.py`:

.. code-block:: python
   :caption: settings.py

    STORAGES = {
        ...
        "staticfiles": {"BACKEND": "app.storage.GZIPManifestStorage"},
    }


Using with other storages
=========================

You can also use your own custom storage, for example, if you want to use S3
for your assets.

Your storage needs to inherit from ``PipelineMixin``. To add cache-busting,
also inherit from Django's
:py:class:`~django.contrib.staticfiles.storage.ManifestFilesMixin`.

.. code-block:: python
   :caption: app/storage.py

    from django.contrib.staticfiles.storage import ManifestFilesMixin
    from pipeline.storage import PipelineMixin
    from storages.backends.s3 import S3Storage

    class S3PipelineManifestStorage(PipelineMixin, ManifestFilesMixin, S3Storage):
        """A storage backend that uses Amazon S3 for assets.

        This also mixes in ManifestFilesMixin to provide cache busting.
        """
        pass

.. code-block:: python
   :caption: settings.py

    STORAGES = {
        ...
        "staticfiles": {"BACKEND": "app.storage.S3PipelineManifestStorage"},
    }
