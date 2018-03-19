from django.template.loader import render_to_string
from citeproc.source.bibtex import bibtex
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import formatter
from citeproc import Citation, CitationItem
import io

bib_source = open('xampl.bib','r', encoding='utf-8').read()
bib = bibtex.BibTeX(io.StringIO(bib_source), encoding='utf-8')
# load a CSL style (from the current directory)

bib_style = CitationStylesStyle('harvard1', 'ru-ru', validate=False)

# Create the citeproc-py bibliography, passing it the:
# * CitationStylesStyle,
# * BibliographySource (BibTeX in this case), and
# * a formatter (plain, html, or you can write a custom formatter)

bibliography = CitationStylesBibliography(bib_style, bib)

citation = Citation([CitationItem('sep-montague-semantics')])

bibliography.register(citation)
# Processing citations in a document needs to be done in two passes as for some
# CSL styles, a citation can depend on the order of citations in the
# bibliography and thus on citations following the current one.
# For this reason, we first need to register all citations with the
# CitationStylesBibliography.

for elem in bibliography.bibliography():
    print(elem)