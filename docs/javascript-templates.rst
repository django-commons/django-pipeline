.. _ref-javascript-templates:

====================
JavaScript Templates
====================

Pipeline allows you to use JavaScript templates along with your JavaScript views.
To use your JavaScript templates, just add them to your ``JAVASCRIPT`` group:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "JAVASCRIPT": {
            "application": {
                "source_filenames": (
                    "js/application.js",
                    "js/templates/*/*.jst",
                ),
                "output_filename": "js/application.js"
            }
        },
    }

For example, if you have the following template ``js/templates/photo/detail.jst``:

.. code-block:: erb

    <div class="photo">
      <img src="<%= src %>">
      <div class="caption">
        <%= caption %>
      </div>
    </div>

It will be available from your JavaScript code via ``window.JST``:

.. code-block:: javascript

    JST.photo_detail({ src:"images/baby-panda.jpg", caption:"A baby panda is born" });


Template configuration options
------------------------------

.. confval:: TEMPLATE_FUNC
   :type: ``str``
   :default: ``"template"``

   The JavaScript function that compiles your templates.

   By default, Pipeline uses a variant of `Micro Templating
   <https://johnresig.com/blog/javascript-micro-templatin/>`_ that is bundled
   with Pipeline. To use another templating library, see
   :ref:`ref-template-libraries`.

.. confval:: TEMPLATE_NAMESPACE
   :type: ``str``
   :default: ``"window.JST"``

   The top-level JavaScript object that your compiled templates are added to.
   For example:

   .. code-block:: python
      :caption: settings.py

       PIPELINE = {
           ...
           "TEMPLATE_NAMESPACE": "window.Template",
       }

.. confval:: TEMPLATE_EXT
   :type: ``str``
   :default: ``".jst"``

   The file extension Pipeline uses to detect templates. For example:

   .. code-block:: python
      :caption: settings.py

       PIPELINE = {
           ...
           "TEMPLATE_EXT": ".mustache",
       }

.. confval:: TEMPLATE_SEPARATOR
   :type: ``str``
   :default: ``"_"``

   The string used in place of the directory separator when naming templates.
   With the default, ``js/templates/photo/detail.jst`` becomes
   ``photo_detail``. For example:

   .. code-block:: python
      :caption: settings.py

       PIPELINE = {
           ...
           "TEMPLATE_SEPARATOR": "/",
       }


.. _ref-template-libraries:

Using it with your favorite template library
--------------------------------------------

Mustache
........

To use it with `Mustache <https://github.com/janl/mustache.js>`_, you need a
small helper. It turns a template string into a function, like the other
template libraries:

.. code-block:: javascript

    Mustache.template = function(templateString) {
        Mustache.parse(templateString);

        return function(view, partials) {
            return Mustache.render(templateString, view, partials);
        };
    };

Load this after ``mustache.js`` and before your templates. Then use these
settings:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "TEMPLATE_EXT": ".mustache",
        "TEMPLATE_FUNC": "Mustache.template",
    }


Handlebars
..........

To use it with `Handlebars <https://handlebarsjs.com/>`_, use the following
settings:

.. code-block:: python
   :caption: settings.py

    PIPELINE = {
        ...
        "TEMPLATE_EXT": ".handlebars",
        "TEMPLATE_FUNC": "Handlebars.compile",
        "TEMPLATE_NAMESPACE": "Handlebars.templates",
    }
