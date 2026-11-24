YUI Compressor
==============

The YUI compressor uses `yui-compressor
<https://yui.github.io/yuicompressor/>`_ for compressing stylesheets and
JavaScript.

To use it for stylesheets, add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "pipeline.compressors.yui.YUICompressor",
    }

To use it for JavaScript:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.yui.YUICompressor",
    }


YUI Compressor configuration options
------------------------------------

.. confval:: YUI_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env yuicompressor"``

   Command line to execute for the YUI compressor program.

   .. warning:: Don't point to ``yuicompressor.jar`` directly. This must be an
                executable script.

.. confval:: YUI_CSS_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`yuicompressor` when compressing
   CSS.

.. confval:: YUI_JS_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`yuicompressor` when compressing
   JavaScript.
