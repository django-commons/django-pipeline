.. _ref-signals:

=======
Signals
=======

List of all signals sent by pipeline.

``css_compressed``
==================

:py:data:`pipeline.signals.css_compressed`

Whenever a css package is compressed, this signal is sent after the
compression.

Arguments sent with this signal:

:sender:
    The :py:class:`pipeline.packager.Packager` instance that compressed the group.

:package:
    The package actually compressed.


``js_compressed``
=================

:py:data:`pipeline.signals.js_compressed`

Whenever a js package is compressed, this signal is sent after the compression.

Arguments sent with this signal:

:sender:
    The :py:class:`pipeline.packager.Packager` instance that compressed the group.

:package:
    The package actually compressed.
