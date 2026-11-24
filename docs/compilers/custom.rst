Write your own compiler class
=============================

You can write your own compiler class, for example if you want to implement
other types of compilers.

To do so, you just have to create a class that inherits from
``pipeline.compilers.CompilerBase`` and implements ``match_file`` and
``compile_file`` when needed.


Example
-------

A custom compiler for an imaginary compiler called jam:

.. code-block:: python
   :caption: jam/compilers.py

    from pipeline.compilers import CompilerBase

    class JamCompiler(CompilerBase):
        output_extension = "js"

        def match_file(self, filename):
            return filename.endswith(".jam")

        def compile_file(self, infile, outfile, outdated=False, force=False):
            if not outdated and not force:
                return

            return jam.compile(infile, outfile)

Then add it to your :doc:`settings </configuration>`:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "COMPILERS": (
            "jam.compilers.JamCompiler",
        ),
    }
