Scripts to Generate Dash Docsets
================================

This is a collection of scripts to download and index various
documentation to the [Dash][] docset format. Results have been tested to
work with Emacs and [dash-docs][], but will probably work with all
applications that support the docset format.

[Dash]: https://kapeli.com/docsets
[dash-docs]: https://github.com/dash-docs-el/dash-docs

To generate a docset, e.g. Python, run the following command.

    ./update.sh Python.docset

To generate all docsets, use `*.docset` as the argument above.
