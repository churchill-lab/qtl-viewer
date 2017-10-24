# Data Structures in QTL Viewer

The QTL Viewer makes use of R and several different libraries. This document is intended to explain the format of the main `RData` file.

> Please note that some data elements are pre-computed.

## Elements

The following elements should be in the `RData` file.  

* [`genome_build`](#genome_build) - string specifying the genome build
* [`genoprobs`](#genoprobs) - the genotype probabilities 
* [`K`](#kinship) - the kinship matrix
* [`map`](#map) - list of one element per chromosome, with the genomic position of each marker
* [`markers`](#markers) - marker names and positions

*Exact case of the variable names is important*

------------

#### `genome_build`<a name="genome_build"></a> *OPTIONAL*

- **Description:** This is the genome build. For example, "GRCm38"

- **R data type:** character

Please see the documentation at [Ensembl](http://www.ensembl.org/info/website/archives/assembly.html) for build information.

------------

#### `genoprobs`<a name="genoprobs"></a> *REQUIRED*

- **Description:** This is the genotype probabilities.

- **R data type:** [calc_genoprobs](https://github.com/rqtl/qtl2geno)

Please see the documentation at [R/qtl2geno](https://github.com/rqtl/qtl2geno).

------------

#### `K`<a name="kinship"></a> *REQUIRED*

- **Description:** The kinship matrix

- **R data type:** [list](http://www.r-tutor.com/r-introduction/list)

------------

#### `map`<a name="map"></a> *REQUIRED*

- **Description:** A list of one element per chromosome, with the genomic position of each.

- **R data type:** [list](http://www.r-tutor.com/r-introduction/list)

------------

#### `markers`<a name="markers"></a> *REQUIRED*

- **Description:** R data type: [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `marker` | character | name of the marker
| `chrom` | string | the chromosome
| `pos` | numeric | position in megabases, (*For example 0.0-200.0*)

`rownames` must also match the names of the `marker` column

------------

## Configurable Elements

The following element is a *special* element and there must be at least per `RData` file.

* [`dataset.*`](#data_elements) - special element

**mRNA**, **protein**, and **phenotype** data sets CAN be configured by `dataset.*` elements.

### `dataset.*`<a name="data_elements"></a>

The `*` part should be alpha-numeric text (underscores are allowed) that describes succinctly your data element.  There must be at least 1 `dataset.*` elements per `RData` file.  These elements will allow you to store multiple **mRNA**, **protein**, and **phenotype** data sets.

For example, there could be `dataset.mRNA` and `dataset.mRNA2` to store 2 mRNA datasets.  The text for the `*` part should be any text that make sense to you or your dataset.  What is defined in the `dataset.*` element is what is more important.

#### mRNA and protein `dataset.*`

The following elements should be in each **mRNA** and **protein** `dataset.*`

* `annots` - annotations of the mrna or protein data
* `covar` - matrix of covariates data, samples (rows) x covariates (columns)
* `covar_factors` - specific information about the covars
* `datatype` - type of data, either **mRNA** or **protein**
* `display_name` - simple display name for the viewer
* `ensembl_version` - version of Ensembl used for annot locations
* `expr` -  expression data, samples (rows) x mrna (columns)
* `raw` - matrix of raw mrna data (counts out of [EMASE](http://churchill-lab.github.io/emase/))
* `samples` - sample annotations

#### phenotype `dataset.*`

The following elements should be in each **phenotype** `dataset.*`

* `annots` - data dictionary
* `covar` - matrix of covariates data, samples (rows) x covariates (columns)
* `covar_factors` - specific information about the covars
* `datatype` - type of data, must be **phenotype**
* `display_name` - simple display name for the viewer
* `pheno` -  data, samples (rows) x mrna (columns)
* `samples` - sample annotations




