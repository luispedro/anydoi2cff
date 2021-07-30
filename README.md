# Any-DOI 2 CFF

[![Automated Tests](https://github.com/luispedro/anydoi2cff/actions/workflows/python-package.yml/badge.svg)](https://github.com/luispedro/anydoi2cff/actions/workflows/python-package.yml)

Very simple CFF generator.

Usage example:

```bash
python ./anydoi2cff/main.py http://doi.org/10.5334/jors.161
```

The `CITATION.cff` format mandates a `version` field, which is set to `0.0.0`.
You should probably edit it to fit your needs.

Dependencies:

You can install all the dependencies with

```bash
pip install -r requirements.txt
```

- requests
- pyyaml


License: MIT
Author: Luis Pedro Coelho

