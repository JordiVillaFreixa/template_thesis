# $Id: thesisCreator.py,v 1.2 2009/04/15 16:16:47 alopez Exp $
import os

os.system('pdflatex main.tex')
os.system('bibtex main')
os.system('pdflatex main')
os.system('pdflatex main')
os.system('rm main.bbl main.log main.aux main.blg main.toc main.lof main.lot')
