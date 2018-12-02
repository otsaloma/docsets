Scripts to Generate Dash Docsets
================================

This is a collection of scripts to download and index various
documentation to the [Dash][] docset format. Results have been tested to
work with Emacs and [helm-dash][], but will probably work with all
applications that support the docset format.

[Dash]: https://kapeli.com/docsets
[helm-dash]: https://github.com/areina/helm-dash

To generate these docsets, you'll need Wget, Python 3, Requests and
Beautiful Soup 4 (bs4). To generate a docset, e.g. Python, run
`./build Python.docset`; to generate all docsets, run `./build *.docset`.
