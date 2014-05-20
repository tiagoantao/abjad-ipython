# -*- coding: utf-8 -*-
"""
    abjad-ipython
    ~~~~~~~~~~~~~

    Interface between IPython Notebook and Abjad.

    :copyright: Copyright 2014 by Tiago Antao.
    :license: GNU Affero, see LICENSE for details.
"""
import os
import shutil
import tempfile

from IPython.core.display import display_png

from wand.image import Image as wimg  # There is another Image from ipython

from abjad.tools import systemtools, topleveltools


def _get_png(expr):
    """Calls lilypond and converts output to (multi-page) PNGs."""
    pngs = []
    tmpdir = tempfile.mkdtemp()
    agent = topleveltools.persist(expr)
    result = agent.as_ly(tmpdir + os.sep + 'out.ly')
    ly_file_path, abjad_formatting_time = result
    cmd = 'lilypond --png -o%s/out %s/out.ly' % (tmpdir, tmpdir)
    result = systemtools.IOManager.spawn_subprocess(cmd)
    try:
        imgs = [wimg(filename=tmpdir + os.sep + 'out.png')]
    except:
        #This might be a multipage output
        #We are going to send all pages
        imgs = []
        for i in range(1000):  # Lets hope you do not have more than 1000 pages
            try:
                imgs.append(wimg(filename=tmpdir + os.sep +
                                 'out-page%d.png' % (i + 1)))
            except:
                if i == 0:  # No images
                    raise
                else:
                    break

    for img in imgs:
        img.trim()
        img.save(filename=tmpdir + os.sep + 'trim.png')
        f = open(tmpdir + os.sep + 'trim.png', 'rb')
        png = f.read()
        pngs.append(png)
        f.close()
    shutil.rmtree(tmpdir)
    return pngs


def show(expr):
    """A replacement for Ajbad's show function for IPython Notebook"""
    assert '__illustrate__' in dir(expr)
    pngs = _get_png(expr)
    for png in pngs:
        display_png(png, raw=True)
