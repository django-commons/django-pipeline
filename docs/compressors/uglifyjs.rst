UglifyJS
========

The UglifyJS compressor uses `UglifyJS <https://lisperator.net/uglifyjs/>`_ to
compress JavaScript.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.uglifyjs.UglifyJSCompressor",
    }


UglifyJS configuration options
------------------------------

.. confval:: UGLIFYJS_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env uglifyjs"``

   Command line to execute for the UglifyJS program.

.. confval:: UGLIFYJS_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`uglifyjs`.
