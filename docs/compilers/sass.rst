SASS
====

The SASS compiler uses `SASS <https://sass-lang.com/>`_ to compile SASS to CSS.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.sass.SASSCompiler",
        ),
    }


SASS configuration options
--------------------------

.. confval:: SASS_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env sass"``

   Command line to execute for sass program.

.. confval:: SASS_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`sass`.
