Closure Compiler
================

The Closure compressor uses `Google Closure Compiler
<https://developers.google.com/closure/compiler>`_ to compress JavaScript.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.closure.ClosureCompressor",
    }


Closure Compiler configuration options
--------------------------------------

.. confval:: CLOSURE_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env closure"``

   Command line to execute for the Closure Compiler program.

   .. warning:: Don't point to ``compiler.jar`` directly. This must be an
                executable script.

.. confval:: CLOSURE_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`closure`.
