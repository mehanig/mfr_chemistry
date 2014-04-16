# -*- coding: utf-8 -*-

from mfr.core import FileHandler, get_file_extension

from mfr_format.render import render_html

__version__ = '0.1.0'

EXTENSIONS = [
    # TODO: finish this list
]


class Handler(FileHandler):
    # Renderers and exporters are callables
    renderers = {
        'html': render_html
    }

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS