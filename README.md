# README

## Installation Guide

1. Install a TeX distribution, there are two options available:
    1. If you would like a full TeX distribution, install [TeX Live](https://www.tug.org/texlive/) or [MacTeX](https://www.tug.org/mactex/).
    2. If you would like a smaller distribution, install [MiKTeX](https://miktex.org/).
2. Install Pygments by running `pip install Pygments` in the command line.
3. Make sure `Pygments` is in the `PATH` environment variable, (ensuring it is above any other LaTeX PATHs on windows)

## Usage Guide

To build this document you have two options:

### 1 - Full Build

- On \*nix, run: `sh build.bat`
- On Windows, run: `.\build.bat`

### 2 - Short Build

If you have not used the bibliography or added a reference then use this build script.

- On \*nix, run: `sh short_build.bat`
- On Windows, run: `.\short_build.bat`
