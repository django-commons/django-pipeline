JSMin
=====

The jsmin compressor uses the `jsmin <https://github.com/tikitu/jsmin/>`_
library to compress JavaScript.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.jsmin.JSMinCompressor",
    }

Install the jsmin library:

.. code-block:: console

    $ pip install jsmin
