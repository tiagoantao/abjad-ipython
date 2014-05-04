from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.display import display_png


@magics_class
class AbjadMagic(Magics):

    @line_magic
    def show(self, line=''):
        display_png(open('/home/tra/.abjad/output/%s' % '0010.preview.png',
                         'rb').read(),
                    raw=True)


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    global _loaded
    if not _loaded:
        ip.register_magics(AbjadMagic)
        _loaded = True

_loaded = False
