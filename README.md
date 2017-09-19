# LTR-Harvest-Reformat

Correct sequence names in LTR_Harvest GFF3 output.

# Contents

* [Options and usage](#options-and-usage)
    * [Installing LTR-HR](#installing-ltr-hr)
    * [Example usage](#example-usage)
    * [Standard options](#standard-options)
* [License](#license)

# Options and usage

## Installing LTR-HR

Clone from this repository:

```bash
git clone https://github.com/Adamtaranto/LTR-Harvest-Reformat.git && cd LTR-Harvest-Reformat
```

## Example usage

```bash
./LTR-Harvest-Reformat.py -i LTR_Harvest_annot.gff3 -d results -o renammed_LTR_Harvest_annot.gff3
```

**Output:**
  - results/renammed_LTR_Harvest_annot.gff3

## Standard options

```
Usage: ./LTR-Harvest-Reformat.py [-h] [--version] -i INFILE [-d OUTDIR] [-o GFFOUT]

Correct sequence names in LTR_Harvest GFF3 output.

optional arguments:
  -h, --help        Show this help message and exit.
  --version         Show program's version number and exit.
  -i, --infile      GFF3 file from LTR_Harvest.
  -d, --outDir      Optional: Set output directory.
  -o, --gffOut      Optional: Set alternative name for output file.
```

# License

Software provided under MIT license.