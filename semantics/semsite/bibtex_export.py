from django.template.loader import render_to_string
from citeproc.source.bibtex import bibtex
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import formatter
from citeproc import Citation, CitationItem
import io
import os
from semantics.settings import BASE_DIR

def warn(citation_item):
    print("WARNING: Reference with key '{}' not found in the bibliography."
          .format(citation_item.key))


def make_citation_by_string(publications):
    bib_str = render_to_string('semsite/export/publications.bib', {'publications': publications})
    bib = bibtex.BibTeX(io.StringIO(bib_str), encoding='utf-8')
    bib_style = CitationStylesStyle('gost-r-7-0-5-2008', 'ru-ru', validate=False)
    bibliography = CitationStylesBibliography(bib_style, bib)
    citation_items = [CitationItem(key) for key in bib]
    citation = Citation(citation_items)
    bibliography.register(citation)
    return bibliography.cite(citation, warn)

def make_bibliography_entry_by_string(publications):
    bib_str = render_to_string('semsite/export/publications.bib', {'publications': publications})
    bib = bibtex.BibTeX(io.StringIO(bib_str), encoding='utf-8')
    bib_style = CitationStylesStyle(os.path.join(BASE_DIR,'semsite/gost-r-7-0-5-2008'), 'ru-ru', validate=False)
    bibliography = CitationStylesBibliography(bib_style, bib)
    citation_items = [CitationItem(key) for key in bib]
    citation = Citation(citation_items)
    bibliography.register(citation)
    return bibliography.bibliography()
