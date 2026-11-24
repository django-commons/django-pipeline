LESS
====

The LESS compiler uses `LESS <https://lesscss.org/>`_ to compile LESS to CSS.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.less.LessCompiler",
        ),
    }


LESS configuration options
--------------------------

.. confval:: LESS_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env lessc"``

   Command line to execute for lessc program.

.. confval:: LESS_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`lessc`.
