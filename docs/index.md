# Home

## A few notes on Material for MkDocs

From [mkdocs.org](https://www.mkdocs.org),
> Material for MkDocs is a powerful documentation framework on top of MkDocs, a static site generator for project documentation.

This framework is similar to documentation platforms used by [Virginia Tech ARC](https://www.docs.arc.vt.edu/index.html) and the [Virginia Tech Cyber Range (albeit with a custom homepage)](https://kb.virginiacyberrange.org/index.html). It is also similar to Bookdown, but unlike Bookdown, MkDocs does not support intrinsic/dynamic R code (etc.).

There is a mock-up article under the [Molecular Dynamics tab](Molecular Dynamics/MD Analysis/PCA.md) that uses some of the features we might be interested in.

### Other stuff

* Can be hosted and published on GitHub/GitHub Pages (which is where this mock-up is now!)
    * Page deployment can also be automated.
* Very customizable, lots of extensions, uses markdown.
* Can view changes live via `mkdocs serve`.

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        assets/   # Images and other media embedded in articles.
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.