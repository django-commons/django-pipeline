TypeScript
==========

The TypeScript compiler uses `TypeScript <https://www.typescriptlang.org/>`_ to
compile TypeScript code to JavaScript.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.typescript.TypeScriptCompiler",
        ),
    }


TypeScript configuration options
--------------------------------

.. confval:: TYPE_SCRIPT_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env tsc"``

   Command line to execute for TypeScript program.

.. confval:: TYPE_SCRIPT_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`tsc`.
