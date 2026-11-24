Yuglify
=======

The Yuglify compressor uses `yuglify <https://github.com/yui/yuglify>`_
for compressing stylesheets and JavaScript.

To use it for stylesheets, add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    }

To use it for JavaScript:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.yuglify.YuglifyCompressor",
    }


Yuglify configuration options
-----------------------------

.. confval:: YUGLIFY_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env yuglify"``

   Command line to execute for the Yuglify program.

.. confval:: YUGLIFY_CSS_ARGUMENTS
   :type: ``str``
   :default: ``"--terminal"``

   Additional arguments to pass to :command:`yuglify` when compressing CSS.

.. confval:: YUGLIFY_JS_ARGUMENTS
   :type: ``str``
   :default: ``"--terminal"``

   Additional arguments to pass to :command:`yuglify` when compressing
   JavaScript.
