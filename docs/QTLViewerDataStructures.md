# Data Structures in QTL Viewer

The QTL Viewer makes use of R and several different libraries. This document is intended to explain the format of the main `RData` file.

> Please note that some data elements are pre-computed.

The following sections try to explain what each element is required and which is optional, along with the structure.

**mRNA** and **protein** data sets are treated similarly.  **phenotype** data sets have a different structure.  This will hopefully be made clear in the [`dataset.*`](#data_elements) section below.

* [mRNA and protein `dataset`](#mrna_dataset)
* [phenotype `dataset`](#pheno_dataset)


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

- **Description:** marker information 

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `marker` | character | name of the marker
| `chrom` | character | the chromosome
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

------------

### mRNA and protein <a name="mrna_dataset"></a>`dataset.*`

The following elements should be in each **mRNA** and **protein** `dataset.*`

* [`annots`](#mrna_annots) - annotations of the mrna or protein data
* [`covar`](#mrna_covar) - matrix of covariates data, samples (rows) x covariates (columns)
* [`covar_factors`](#mrna_covar_factors) - specific information about the covars
* [`datatype`](#mrna_datatype) - type of data, either **mRNA** or **protein**
* [`display_name`](#mrna_display_name) - simple display name for the viewer
* [`ensembl_version`](#mrna_ensembl_version) - version of Ensembl used for annot locations
* [`expr`](#mrna_expr) -  expression data, samples (rows) x mrna (columns)
* [`raw`](#mrna_raw) - matrix of raw mrna data (counts out of [EMASE](http://churchill-lab.github.io/emase/))
* [`samples`](#mrna_samples) - sample annotations

------------

#### `annots`<a name="mrna_annots"></a> *REQUIRED*

- **Description:** annotations for **mRNA** or **protein**

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `id` | character | Ensembl ID
| `symbol` | character | the symbol
| `chr` | character | chromosome
| `start` | numeric | start position in megabases, (*For example 0.0-200.0*)
| `end` | numeric | end position in megabases, (*For example 0.0-200.0*)
| `strand` | numeric | -1 for negative, 1 for positive
| `middle_point` | numeric | middle point in megabases, (*For example 0.0-200.0*)
| `nearest_marker` | numeric | nearets marker in megabases, (*For example 0.0-200.0*)

`rownames` must also match the names of the `id` column

------------

#### `covar`<a name="mrna_covar"></a> *REQUIRED*

- **Description:** covariates data, samples (rows) x covariates (columns)

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

------------

#### `covar_factors`<a name="mrna_covar_factors"></a> *REQUIRED*

- **Description:** covar information

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `column_name` | character | column name in [`covar`](#mrna_covar)
| `display_name` | character | display name for the viewer

------------

#### `datatype`<a name="mrna_datatype"></a> *REQUIRED*

- **Description:** **mRNA** or **protein**

- **R data type:** character

------------

#### `display_name`<a name="mrna_display_name"></a> *OPTIONAL*

- **Description:** simple display name for the viewer

- **R data type:** character

------------

#### `ensembl_version`<a name="mrna_ensembl_version"></a> *OPTIONAL*

- **Description:** Ensembl version number used in annotations

- **R data type:** numeric

Please see the documentation at [Ensembl](http://www.ensembl.org/info/website/archives/assembly.html) for build information.

------------

#### `expr`<a name="mrna_expr"></a> *REQUIRED*

- **Description:** expression data, [`samples`](#mrna_samples) (rows) x [`annots`](#mrna_annots) (columns)

- **R data type:** [matrix](http://www.r-tutor.com/r-introduction/matrix)

------------

#### `raw`<a name="mrna_raw"></a> *REQUIRED*

- **Description:** raw expression data, [`samples`](#mrna_samples) (rows) x [`annots`](#mrna_annots) (columns)

- **R data type:** [matrix](http://www.r-tutor.com/r-introduction/matrix)

------------

#### `samples`<a name="mrna_samples"></a> *REQUIRED*

- **Description:** sample annotations

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `id` | character | Mouse ID

`rownames` must also match the names of the `id` column

Extra columns can be included, and will be rendered in the viewer. For example,

> | id | Sex | Age | Description |
> | ----------- | ---------- | ---------- | ---------- |
> | DO-001 | F | 12 | some description
> | DO-002 | F | 14 | another description
> | DO-203 | M | 1 | yet another description

------------

### phenotype <a name="pheno_dataset"></a>`dataset.*`

The following elements should be in each **phenotype** `dataset.*`

* [`annots`](#pheno_annots) - data dictionary 
* [`covar`](#pheno_covar) - matrix of covariates data, samples (rows) x covariates (columns)
* [`covar_factors`](#pheno_covar_factors) - specific information about the covars
* [`datatype`](#pheno_datatype) - type of data, must be **phenotype**
* [`display_name`](#pheno_display_name) - simple display name for the viewer
* [`pheno`](#pheno_pheno) -  data, samples (rows) x mrna (columns)
* [`samples`](#pheno_samples) - sample annotations

------------

#### `annots`<a name="pheno_annots"></a> *REQUIRED*

- **Description:** data dictionary for phenotypes

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

TODO: DEFINE DATA DICTIONARY
------------

#### `covar`<a name="pheno_covar"></a> *REQUIRED*

- **Description:** covariates data, samples (rows) x covariates (columns)

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

------------

#### `covar_factors`<a name="pheno_covar_factors"></a> *REQUIRED*

- **Description:** covar information

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `column_name` | character | column name in [`covar`](#mrna_covar)
| `display_name` | character | display name for the viewer

------------

#### `datatype`<a name="pheno_datatype"></a> *REQUIRED*

- **Description:** MUST BE **phenotype**

- **R data type:** character

------------

#### `display_name`<a name="pheno_display_name"></a> *OPTIONAL*

- **Description:** simple display name for the viewer

- **R data type:** character

------------

#### `pheno`<a name="pheno_pheno"></a> *REQUIRED*

- **Description:** pheno data, [`samples`](#pheno_samples) (rows) x [`annots`](#pheno_annots) (columns)

- **R data type:** [matrix](http://www.r-tutor.com/r-introduction/matrix)

------------

#### `samples`<a name="pheno_samples"></a> *REQUIRED*

- **Description:** sample annotations

- **R data type:** [data.frame](http://www.r-tutor.com/r-introduction/data-frame)

The following column names must be present:

| column_name | column_type | description |
| ----------- | ---------- | ---------- |    
| `id` | character | Mouse ID

`rownames` must also match the names of the `id` column

Extra columns can be included, and will be rendered in the viewer. For example,

> | id | Sex | Age | Description |
> | ----------- | ---------- | ---------- | ---------- |
> | DO-001 | F | 12 | some description
> | DO-002 | F | 14 | another description
> | DO-203 | M | 1 | yet another description

------------
