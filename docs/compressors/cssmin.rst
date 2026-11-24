CSSMin
======

The cssmin compressor uses the `cssmin
<https://github.com/jbleuzen/node-cssmin>`_ command to compress stylesheets. To
use it, add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "pipeline.compressors.cssmin.CSSMinCompressor",
    }


CSSMin configuration options
----------------------------

.. confval:: CSSMIN_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env cssmin"``

   Command line to execute for cssmin program.


.. confval:: CSSMIN_ARGUMENTS
   :type: ``str``
   :default: ``""``

   Additional arguments to pass to :command:`cssmin`.
