# -*- coding: utf-8 -*-
from mfr.core import FileHandler, get_file_extension
from mfr_chemistry.render import render_chemistry_tag

EXTENSIONS = [
    '.pdb',
    '.mol',
    #Add more file extensions
]


class Handler(FileHandler):
    """The chemsitry file handler."""
    renderers = {
        'html': render_chemistry_tag,
    }

    exporters = exporters

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONSNS