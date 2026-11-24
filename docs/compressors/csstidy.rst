CSSTidy
=======

The CSStidy compressor uses `CSStidy <https://csstidy.sourceforge.net/>`_ to
compress stylesheets.

To use it for stylesheets, add this to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "CSS_COMPRESSOR": "pipeline.compressors.csstidy.CSSTidyCompressor",
    }


CSSTidy configuration options
-----------------------------

.. confval:: CSSTIDY_BINARY
   :type: ``str``
   :default: ``"/usr/bin/env csstidy"``

   Command line to execute for csstidy program.

.. confval:: CSSTIDY_ARGUMENTS
   :type: ``str``
   :default: ``"--template=highest"``

   Additional arguments to pass to :command:`csstidy`.
