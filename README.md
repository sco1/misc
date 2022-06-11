# misc
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sco1-misc)](https://pypi.org/project/sco1-misc/)
[![PyPI](https://img.shields.io/pypi/v/sco1-misc)](https://pypi.org/project/sco1-misc/)
[![PyPI - License](https://img.shields.io/pypi/l/sco1-misc?color=magenta)](https://github.com/sco1/sco1-misc/blob/main/LICENSE)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/sco1-misc/main.svg)](https://results.pre-commit.ci/latest/github/sco1/sco1-misc/main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-VSCode.dev-blue)](https://vscode.dev/github.com/sco1/sco1-misc)

A collection of miscellaneous helpers.

## The Help
### `sco1_misc.prompts`
Helper wrappers for [`Tkinter`'s selection dialogs](https://docs.python.org/3/library/dialog.html)

  * `prompt_for_file(title: str, start_dir: pathlib.Path, multiple: bool, filetypes: list[tuple[str, str]])`
  * `prompt_for_dir(title: str, start_dir: pathlib.Path)`

### `csvdatetrim`
A CLI tool for date windowing CSV log files

**NOTE:** The following assumptions are made about the input CSV file:
  * The CSV file contains a column named `"Time"`, with timestamps formatted as `MM/DD/YYYY HH:MM:SS` 
  * The CSV file ends on the same date as the specified date filter

#### Input Parameters
| Parameter        | Description                           | Type         | Default                         |
|------------------|---------------------------------------|--------------|---------------------------------|
| `--log-filepath` | Path to log file to trim.             | `Path\|None` | GUI Prompt                      |
| `--test_date`    | Trim date selection, as `YYYY-MM-DD`. | `str`        | Today's date                    |
| `--out-filename` | Output filename.<sup>1,2,3</sup>      | `str\|None`  | `<in_filename>_<test_date>.csv` |

1. Output file is saved to the parent directory of `--log-filepath`
2. Trimming will be aborted if `--out-filename` matches `--log-filepath`
3. Any existing data will be discarded

## Contributing
### Development Environment
This project uses [Poetry](https://python-poetry.org/) to manage dependencies. With your fork cloned to your local machine, you can install the project and its dependencies to create a development environment using:

```bash
$ poetry install
```

A [pre-commit](https://pre-commit.com) configuration is also provided to create a pre-commit hook so linting errors aren't committed:

```bash
$ pre-commit install
```
