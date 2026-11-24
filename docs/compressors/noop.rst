No-Op Compressors
=================

The No-Op compressors will concatenate files, but not perform any compression.
This is useful for debugging errors that can occur when poorly-written
JavaScript files get concatenated together.

To use it, add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "pipeline.compressors.NoopCompressor",
        "JS_COMPRESSOR": "pipeline.compressors.NoopCompressor",
    }
