from pipeline.compressors import CompressorBase


class JSMinCompressor(CompressorBase):
    """JS compressor based on the Python library jsmin."""

    def compress_js(self, js):
        from jsmin import jsmin

        return jsmin(js)
