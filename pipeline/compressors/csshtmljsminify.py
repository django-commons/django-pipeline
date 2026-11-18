from contextlib import redirect_stdout
from io import StringIO

from pipeline.compressors import CompressorBase


class CssHtmlJsMinifyCompressor(CompressorBase):
    """
    CSS, HTML and JS compressor based on the Python library css-html-js-minify
    (https://pypi.org/project/css-html-js-minify/).
    """

    def compress_css(self, css):
        from css_html_js_minify import css_minify

        return css_minify(css)

    def compress_js(self, js):
        from css_html_js_minify import js_minify

        # This library always prints out an annoying warning about not supporting modern
        # JavaScript. Suppress that.
        with redirect_stdout(StringIO()):
            return js_minify(js)
