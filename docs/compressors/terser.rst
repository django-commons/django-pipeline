Terser
======

`Terser <https://github.com/terser/terser>`_ is a JavaScript parser and
mangler/compressor toolkit for ES6+. It has been designed as a successor of
``uglify-es`` and ``uglify-js``. The compressor works with ES5 and ES6 and
regular ``.js`` file endings.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JS_COMPRESSOR": "pipeline.compressors.terser.TerserCompressor",
    }


Terser configuration options
----------------------------

.. confval:: TERSER_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env terser"``

   Command line to execute for the terser program.

.. confval:: TERSER_ARGUMENTS
   :type: ``str``
   :default: ``"--compress"``

   Additional arguments to pass to :command:`terser`.
