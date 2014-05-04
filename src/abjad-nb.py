import os
import shutil
import tempfile

from IPython.core.display import display_png

from wand.image import Image

from abjad.tools import systemtools, topleveltools


def _get_png(expr):
    tmpdir = tempfile.mkdtemp()
    agent = topleveltools.persist(expr)
    result = agent.as_ly(tmpdir + os.sep + 'out.ly')
    ly_file_path, abjad_formatting_time = result
    cmd = 'lilypond --png -o%s/out %s/out.ly' % (tmpdir, tmpdir)
    result = systemtools.IOManager.spawn_subprocess(cmd)
    img = Image(filename=tmpdir + os.sep + 'out.png')
    img.trim()
    img.save(filename=tmpdir + os.sep + 'trim.png')
    f = open(tmpdir + os.sep + 'trim.png', 'rb')
    png = f.read()
    f.close()
    shutil.rmtree(tmpdir)
    return png


def show(expr):
    assert '__illustrate__' in dir(expr)
    png = _get_png(expr)
    display_png(png, raw=True)
