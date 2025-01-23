
# Installation Guide for WonderPeaks_preprocessing

## 1. Prerequisites

### 1.1. Anaconda or Miniconda
Used to load requirements to run preprocessing (Method 5) and WonderPeaks (Method 6 or Method 7). A user guide for Anaconda can be found here: [Anaconda Getting Started](https://docs.anaconda.com/anaconda/getting-started/).

### 1.2. Python
Python can be installed within Anaconda or Miniconda.

### 1.3. Jupyter Notebooks
Jupyter Notebooks are used to execute all functions in this method. A beginner’s user guide for Jupyter Notebooks can be found here: [Jupyter Notebook Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/).

**CAUTION:** For yeast genomes, ensure a compute environment with at least 20 cores, 8 GB of RAM, and 30 GB of available disk space.

## 2. Install Preprocessing Functions

### 2.1. Steps
1. Execute the following in your terminal:
    ```bash
    conda create -n WP_preprocessing
    ```
2. Activate the environment:
    ```bash
    conda activate WP_preprocessing
    ```
3. Update the environment with dependencies:
    ```bash
    conda env update --file environment.yml --name <current_environment_name>
    ```
    **NOTE:** Download `environment.yml` from [WonderPeaks Preprocessing GitHub](https://github.com/mgarber21/
### 3.2. Summary
These steps create dedicated Conda environments for preprocessing and WonderPeaks, isolating dependencies and preventing conflicts with other software. Always deactivate the environment when not in use to avoid accidental modifications and free up system resources.

## 3. Download Jupyter Notebooks and Templates
1. Download the required Jupyter Notebooks and templates from the [WonderPeaks GitHub Repository](https://github.com/mgarber21/WonderPeaks.git).
2. Upload the downloaded files to the operating system containing your raw data.

**NOTE:** The Jupyter Notebooks contain scripts and templates necessary for preprocessing for WonderPeaks, and PeakStream workflows. Ensure the paths and directories align correctly.

## 5. Create Data Directory
1. Create a data directory:
    ```bash
    mkdir {data_directory}
    # Example
    mkdir /path/to/your/data
    ```
2. Create a raw data subdirectory:
    ```bash
    mkdir {data_directory}/raw_data
    # Example
    mkdir /path/to/your/data/raw_data
    ```
3. Move your raw data files:
    ```bash
    mv {current_path_to_raw_data}/*fastq* {data_directory}/raw_data
    # Example
    mv current/data/path/*fastq* /path/to/your/data/raw_data
    ```

## 4. Create User Inputs File (user_input.csv)
1. Download the template `user_input.csv` from the WonderPeaks GitHub repository.
2. Update the fields in the file:
    - `Data directory`: `/path/to/your/data`
    - `Genome directory`: `/path/to/your/genome`
    - `Genome fasta`: `genome.fasta`
    - `Genome annotation`: `genome_annotation.gtf`
3. Save the updated file to the data directory created earlier.

**CAUTION:** Do not change the file name; WonderPeaks will only recognize it if named `user_input.csv`.

## 5. Create Metadata File (metadata.csv)
1. Download the template `metadata.csv` from the WonderPeaks GitHub repository.
2. Update the fields in the file:
    - `file`: File name (no spaces; include file extension, but not absolute path).
    - `bedgraph`: Specify whether the file should be included in PeakStream (`TRUE` or `FALSE`).
    - `designfactor1` and `designfactor2`: Specify design factors relevant to your experiment (e.g., `treatment` or `strain`).
3. Save the updated file to the data directory.

**CAUTIONS:**
- Design factor columns must not include unique replicate numbers.
- Use underscores (`_`) instead of spaces in design factor names.
- Ensure design factors match columns in `user_input.csv` exactly.

## 6. Preprocessing NGS Data

1. Open the Jupyter Notebook `NGS_Preprocessing.ipynb`in the `Notebook` folder.
2. Activate the `WP_preprocessing` environment.
3. Execute the first cell (Shift + Enter).
4. Update the directory path in the second cell:
    ```python
    Directory = "/path/to/your/data"
    ```
5. Execute preprocessing functions, including:
    - Trimming (FastP)
    - Quality Control (FastQC, MultiQC)
    - Alignment (STAR)
    - Filtering (optional; Samtools)
6. Generate trace files of alignment coverage using BamCoverage.

**NOTE:** Tasks may take hours to complete. If interrupted, rerun the cells to resume from where they left off.
