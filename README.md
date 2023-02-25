# README

## Installation Guide

1. Install a TeX distribution, there are two options available:
    1. If you would like a full TeX distribution, install [TeX Live](https://www.tug.org/texlive/) or [MacTeX](https://www.tug.org/mactex/).
    2. If you would like a smaller distribution, install [MiKTeX](https://miktex.org/).
2. Install Pygments by running `pip install Pygments` in the command line.
3. Add `Pygments` to the `PATH` environment variable, ensuring it is above any other LaTeX PATHs.

## Usage Guide

1. Everytime the bibliography is updated, run `biber main.bcf` to update the bibliography.
2. Run `pdflatex --shell-escpae main.tex` to compile the document to the pdf.
3. Run `pdflatex --shell-escape main.tex` a second time to update the figure list and references as it often fails on the first run.

// TODO: Update Usage guide 