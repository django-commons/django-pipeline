ES6 (Babel)
===========

The ES6 compiler uses `Babel <https://babeljs.io>`_ to convert ES6+ code into
vanilla ES5.

Note that for files to be transpiled properly they must have the file extension
``.es6``

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.es6.ES6Compiler",
        ),
    }


Babel configuration options
---------------------------

.. confval:: BABEL_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env babel"``

   Command line to execute for babel program.

.. confval:: BABEL_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`babel`.
