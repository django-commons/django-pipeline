LiveScript
==========

The LiveScript compiler uses `LiveScript <https://livescript.net/>`_ to compile
LiveScript code to JavaScript.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.livescript.LiveScriptCompiler",
        ),
    }


LiveScript configuration options
--------------------------------

.. confval:: LIVE_SCRIPT_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env lsc"``

   Command line to execute for LiveScript program.

.. confval:: LIVE_SCRIPT_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`lsc`.
