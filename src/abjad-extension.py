import os
import shutil
import tempfile
from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from IPython.core.display import display_png
from abjad.tools import systemtools, topleveltools


def _get_png(expr):
    tmpdir = tempfile.mkdtemp()
    agent = topleveltools.persist(expr)
    result = agent.as_ly(tmpdir + os.sep + 'out.ly')
    ly_file_path, abjad_formatting_time = result
    cmd = 'lilipond --png %s/out.ly -o%s/out'
    systemtools.IOManager.spawn_subprocess(cmd)
    shutil.rmtree(tmpdir)


@magics_class
class AbjadMagic(Magics):

    @magic_arguments()
    @argument('expr')
    @line_magic
    def show(self, params):
        args = parse_argstring(self.show, params)
        expr = args.expr
        print(type(expr))
        print(dir(expr))
        assert '__illustrate__' in dir(expr)
        png = _get_png(expr)
        display_png(png, raw=True)


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    global _loaded
    if not _loaded:
        ip.register_magics(AbjadMagic)
        _loaded = True

_loaded = False
