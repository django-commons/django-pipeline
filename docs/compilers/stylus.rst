Stylus
======

The Stylus compiler uses `Stylus <https://stylus-lang.com/>`_ to
compile stylesheets.

To use it add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "pipeline.compilers.stylus.StylusCompiler",
        ),
    }


Stylus configuration options
----------------------------

.. confval:: STYLUS_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env stylus"``

   Command line to execute for stylus program.

.. confval:: STYLUS_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`stylus`.
