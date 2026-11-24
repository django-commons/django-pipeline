css-html-js-minify
==================

The css-html-js-minify compressor uses the `css-html-js-minify
<https://github.com/ciotto/css-html-js-minify>`_ Python package for compressing
JavaScript and stylesheets.

To use it for stylesheets, add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "pipeline.compressors.csshtmljsminify.CssHtmlJsMinifyCompressor",
    }

To use it for JavaScript:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.csshtmljsminify.CssHtmlJsMinifyCompressor",
    }

Install the css-html-js-minify library:

.. code-block:: console

    $ pip install css-html-js-minify
