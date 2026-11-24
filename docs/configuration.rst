.. _ref-configuration:

=============
Configuration
=============


Configuration and list of available settings for Pipeline. Pipeline settings
are namespaced in a ``PIPELINE`` dictionary in your project settings, e.g.:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        "PIPELINE_ENABLED": True,
        "JAVASCRIPT": {
            "stats": {
                "source_filenames": (
                    "js/jquery.js",
                    "js/d3.js",
                    "js/collections/*.js",
                    "js/application.js",
                ),
                "output_filename": "js/stats.js",
            }
        }
    }


Specifying files
================

You specify groups of files to be compressed in your settings. You can use glob
syntax to select multiple files.

The basic syntax for specifying CSS and JavaScript groups is:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        "STYLESHEETS": {
            "colors": {
                "source_filenames": (
                    "css/core.css",
                    "css/colors/*.css",
                    "css/layers.css"
                ),
                "output_filename": "css/colors.css",
                "extra_context": {
                    "media": "screen,projection",
                },
            },
        },
        "JAVASCRIPT": {
            "stats": {
                "source_filenames": (
                    "js/jquery.js",
                    "js/d3.js",
                    "js/collections/*.js",
                    "js/application.js",
                ),
                "output_filename": "js/stats.js",
            }
        }
    }

.. confval:: STYLESHEETS
   :type: ``dict``
   :default: ``{}``

   The CSS groups. Each key is a group name, and each value is a dictionary
   of :ref:`group options <ref-group-options>`.

.. confval:: JAVASCRIPT
   :type: ``dict``
   :default: ``{}``

   The JavaScript groups. Each key is a group name, and each value is a
   dictionary of :ref:`group options <ref-group-options>`.


.. _ref-group-options:

Group options
-------------

.. confval:: source_filenames
   :type: ``tuple[str, ...]``

   Required.

   The source files to be compressed. The files are concatenated in the order
   given.

.. confval:: output_filename
   :type: ``str``

   Required.

   The filename of the compressed file.

.. confval:: variant
   :type: ``str | None``
   :default: ``None``

   The variant to apply to your CSS. Use ``"datauri"`` to embed images and
   fonts in the CSS. See :ref:`ref-embedding`.

.. confval:: template_name
   :type: ``str | None``
   :default: ``None``

   Name of the template used to render the ``<script>`` tag for a JavaScript
   group, or the ``<link>`` tag for a CSS group.

.. confval:: extra_context
   :type: ``dict``
   :default: ``{}``

   Extra values to add to the template context when the template tags render
   the HTML tags.

   For CSS, if you do not set ``media``, the ``<link>`` tag uses
   ``media="all"``.

   For JavaScript, the default templates support the ``async`` and ``defer``
   attributes:

   .. code-block:: python

       "extra_context": {
           "async": True,
       },

.. confval:: manifest
   :type: ``bool``
   :default: ``True``

   Whether this group should appear in your cache manifest.

.. confval:: compiler_options
   :type: ``dict``
   :default: ``{}``

   Keyword arguments passed to each compiler's ``compile_file`` method. None
   of the built-in compilers use it. It is meant for custom compilers that
   need extra parameters.


Other settings
--------------

.. confval:: PIPELINE_ENABLED
   :type: ``bool``
   :default: ``not settings.DEBUG``

   ``True`` if assets should be compressed, ``False`` if not.

   See :djangosetting:`DEBUG`.

.. confval:: PIPELINE_COLLECTOR_ENABLED
   :type: ``bool``
   :default: ``True``

   ``True`` if assets should be collected during development, ``False`` if
   not.

   This only applies when :confval:`PIPELINE_ENABLED` is ``False``.

.. confval:: PIPELINE_ROOT
   :type: ``str``
   :default: ``settings.STATIC_ROOT``

   The directory where Pipeline looks for compressed output files.

   See :djangosetting:`STATIC_ROOT`.

.. confval:: PIPELINE_URL
   :type: ``str``
   :default: ``settings.STATIC_URL``

   The URL prefix for Pipeline's output files.

   See :djangosetting:`STATIC_URL`.

.. confval:: SHOW_ERRORS_INLINE
   :type: ``bool``
   :default: ``settings.DEBUG``

   ``True`` if errors compiling CSS/JavaScript files should be shown inline at
   the top of the browser window. ``False`` if they should raise exceptions
   (the older behavior).

   This only applies when compiling through the ``{% stylesheet %}`` or
   ``{% javascript %}`` template tags. It does not affect ``collectstatic``.

.. confval:: CSS_COMPRESSOR
   :type: ``str | None``
   :default: ``"pipeline.compressors.yuglify.YuglifyCompressor"``

   Compressor class to apply to CSS files. If empty or ``None``, CSS files are
   not compressed.

   See :doc:`compressors`.

.. confval:: JS_COMPRESSOR
   :type: ``str | None``
   :default: ``"pipeline.compressors.yuglify.YuglifyCompressor"``

   Compressor class to apply to JavaScript files. If empty or ``None``,
   JavaScript files are not compressed.

   See :doc:`compressors`.

   .. note::

      To use the Yuglify compressor, you need to install Yuglify. See
      :doc:`installation` for details.

.. confval:: COMPILERS
   :type: ``list[str]``
   :default: ``[]``

   Compiler classes to run on source files before they are compressed.

   See :doc:`compilers`.

.. confval:: MIMETYPES
   :type: ``tuple[tuple[str, str], ...]``

   Pairs of mimetypes and their file extensions.

   Defaults to:

   .. code-block:: python

       (
           ("text/coffeescript", ".coffee"),
           ("text/less", ".less"),
           ("text/javascript", ".js"),
           ("text/typescript", ".ts"),
           ("text/x-sass", ".sass"),
           ("text/x-scss", ".scss"),
       )

The settings for JavaScript templates (:confval:`TEMPLATE_FUNC`,
:confval:`TEMPLATE_NAMESPACE`, :confval:`TEMPLATE_EXT` and
:confval:`TEMPLATE_SEPARATOR`) are described in :doc:`javascript-templates`.


.. _ref-embedding:

Embedding fonts and images
==========================

You can embed fonts and images directly in your compiled CSS using data URIs.

To do so, set the :confval:`variant` group option to ``"datauri"``:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        "STYLESHEETS": {
            "master": {
                "source_filenames": (
                    "css/core.css",
                    "css/button/*.css",
                ),
                "output_filename": "css/master.css",
                "variant": "datauri",
            },
        },
    }

An asset is embedded only if both of these are true:

- Its path contains a directory named ``embed``.
- It is a font, or its encoded size is under 32,700 bytes.

Overriding embedding settings
-----------------------------

You can change these rules using the following settings:

.. confval:: EMBED_MAX_IMAGE_SIZE
   :type: ``int``
   :default: ``32700``

   The maximum encoded size (in bytes) of an image to embed. Fonts are not
   limited by this setting.

.. confval:: EMBED_PATH
   :type: ``str``
   :default: ``r"[/]?embed/"``

   A regular expression. An asset is only embedded if its path matches.


Rewriting CSS urls
==================

If the source CSS contains relative URLs (i.e. relative to current file), those
URLs will be rewritten so they still point to the right files after the CSS is
combined.


Wrapped JavaScript output
=========================

All JavaScript output is wrapped in an anonymous function:

.. code-block:: javascript

    (function() {
        // JS output...
    }).call(this);

This wrapper makes it harder to pollute the global namespace by accident.

.. confval:: DISABLE_WRAPPER
   :type: ``bool``
   :default: ``False``

   Set to ``True`` to turn off the wrapper.

.. confval:: JS_WRAPPER
   :type: ``str``
   :default: ``"(function() {\n%s\n}).call(this);"``

   The wrapper to use. ``%s`` is replaced with the JavaScript output. For
   example:

   .. code-block:: python
      :caption: settings.py

       PIPELINE = {
           "JS_WRAPPER": "(function() { stuff(); %s })();",
       }
