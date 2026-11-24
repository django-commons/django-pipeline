Write your own compressor class
===============================

You can write your own compressor class, for example if you want to implement
other types of compressors.

To do so, you just have to create a class that inherits from
:py:class:`pipeline.compressors.CompressorBase` and implements ``compress_css``
and/or ``compress_js`` when needed.


Example
-------

A custom compressor for an imaginary compressor called jam:

.. code-block:: python
   :caption: jam/compressors.py

    from pipeline.compressors import CompressorBase

    class JamCompressor(CompressorBase):
        def compress_js(self, js):
            return jam.compress(js)

        def compress_css(self, css):
            return jam.compress(css)

Then add it to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "jam.compressors.JamCompressor",
        "JS_COMPRESSOR": "jam.compressors.JamCompressor",
    }
