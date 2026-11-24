CoffeeScript
============

The CoffeeScript compiler uses `CoffeeScript <https://coffeescript.org/>`_ to
compile CoffeeScript code to JavaScript.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.coffee.CoffeeScriptCompiler",
        ),
    }


CoffeeScript configuration options
----------------------------------

.. confval:: COFFEE_SCRIPT_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env coffee"``

   Command line to execute for coffee program.

.. confval:: COFFEE_SCRIPT_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`coffee`.
