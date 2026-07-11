%global tl_name attinormativi
%global tl_revision 79199

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A complete typographic framework for Italian normative acts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/attinormativi
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attinormativi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attinormativi.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attinormativi.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The attinormativi class provides a complete typographic framework for
Italian normative acts. It manages the hierarchical structure typical of
such documents (books, titles, chapters, sections, articles,
paragraphs), the institutional title page, dedicated indexes (articles,
annexes, definitions), a draft mode with editorial notes, and optional
integration with the cleveref package for Italian-language cross-
references. The class is built on top of the standard book class and is
compatible with pdfLaTeX, XeLaTeX, and LuaLaTeX. La classe attinormativi
fornisce un framework tipografico completo per gli atti normativi
italiani. Gestisce la struttura gerarchica tipica di tali documenti
(libri, titoli, capi, sezioni, articoli, commi), il frontespizio
istituzionale, gli indici dedicati (articoli, allegati, definizioni), la
modalita bozza con note redazionali e l'integrazione opzionale con il
pacchetto cleveref per i riferimenti incrociati in italiano. La classe e
costruita sopra la classe standard book ed e compatibile con pdfLaTeX,
XeLaTeX e LuaLaTeX.

