# Hospital-level Antimicrobial Resistance in Metagenomic Wastewater Surveillance


This repository contains all code and analysis scripts for the study:

**"Metagenomic surveillance identifies a critical antibiotic resistance site in community wastewater"**  
Ishaq Khan¹*, Ihtisham Naeem¹, Shujait Ali¹, Mahnoor Gulbin², Arshad Iqbal¹, Muhammad Shafiq³

¹Center for Biotechnology & Microbiology (CBM), University of Swat, Charbagh 19120, Pakistan  
*Corresponding author: ishaq@uswat.edu.pk

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Availability](#data-availability)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)

---

##  Overview

This study reveals hospital-level antimicrobial resistance (AMR) profiles in untreated community wastewater from Mardan District, Pakistan. Using shotgun metagenomic sequencing, we identified:

- **Last-resort resistance genes** (NDM, IMP, CTX-M, MCR) exclusive to urban sites
- **WHO priority pathogen enrichment** (P. aeruginosa, A. baumannii, E. coli)
- **Strong ARG-MGE associations** indicating high horizontal gene transfer potential
- **Novel ARRI (Antibiotic Resistance Risk Index)** for risk-weighted surveillance

**Key Finding**: Community wastewater (MCW2) exhibits ARRI score of 34.2 (Critical Risk), comparable to hospital effluent, despite no direct healthcare facility connection.

---

## 📁 Repository Structure

```
mardan-wastewater-amr/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── environment.yml                    # Conda environment specification
├── requirements.txt                   # Python dependencies
│
├── scripts/                           # Analysis scripts
│   ├── 01_domain_composition.R        # Domain-level analysis (R)
│   ├── 02_phylum_abundance.R          # Phylum-level analysis (R)
│   ├── 03_ARRI_calculation.py         # ARRI calculation (Python)
│   └── 04_complete_pipeline.ipynb     # Complete analysis pipeline (Jupyter)
│
├── data/                              # Input data files
│   ├── README.md                      # Data description
│   ├── MCW1_MCW2_metadata.csv         # Sample metadata
│   └── sequencing_stats.csv           # Sequencing QC statistics
│
├── results/                           # Output files
│   ├── figures/                       # Generated figures
│   └── tables/                        # Generated tables
│
└── docs/                              # Documentation
    ├── methods.md                     # Detailed methods
    └── supplementary.md               # Supplementary information
```

---

##  Installation

### Prerequisites

- **R** (≥ 4.2.0)
- **Python** (≥ 3.8)
- **Conda** or **Mamba** (recommended for environment management)

### Option 1: Using Conda (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/mardan-wastewater-amr.git
cd mardan-wastewater-amr

# Create conda environment
conda env create -f environment.yml
conda activate mardan-amr
```

### Option 2: Manual Installation

#### R Packages

```r
install.packages(c("ggplot2", "viridis", "dplyr", "tidyr", "scales"))
```

#### Python Packages

```bash
pip install -r requirements.txt
```

Required Python packages:
- pandas ≥ 1.5.0
- numpy ≥ 1.23.0
- matplotlib ≥ 3.6.0
- seaborn ≥ 0.12.0
- scipy ≥ 1.9.0

---

##  Usage

### 1. Domain-Level Composition Analysis

Creates stacked bar plots of Bacteria, Archaea, and Viruses/Phages.

```bash
Rscript scripts/01_domain_composition.R
```

**Outputs**:
- `domain_composition.png` (300 dpi)
- `domain_composition.pdf` (vector)

---

### 2. Phylum-Level Abundance Analysis

Analyzes top 20 bacterial phyla with percentage labels.

```bash
Rscript scripts/02_phylum_abundance.R
```

**Note**: Update `file_path` variable in script to point to your taxonomic annotation file.

**Outputs**:
- `phylum_abundance_TOP20.png`
- `phylum_abundance_TOP20.pdf`

---

### 3. ARRI Calculation

Calculates Antibiotic Resistance Risk Index integrating WHO priority pathogen weighting.

```bash
python scripts/03_ARRI_calculation.py
```

**Example output**:
```
ARRI for MCW2: 34.2 (Critical Risk)
ARRI for MCW1: 8.7 (Moderate Risk)
Fold Change: 3.9x
```

---

### 4. Complete Analysis Pipeline

Comprehensive Jupyter notebook with all analyses.

```bash
jupyter notebook scripts/04_complete_pipeline.ipynb
```

**Includes**:
- Data loading and preprocessing
- ARG differential abundance analysis
- ARG-MGE network analysis
- Risk assessment and visualization
- Statistical testing

---

##  

### Processed Data

All processed data tables are available in the `data/` directory:

| File | Description |
|------|-------------|
| `MCW1_MCW2_metadata.csv` | Sample metadata (location, date, environmental parameters) |
| `sequencing_stats.csv` | Quality control statistics |
| `assembly_stats.csv` | Assembly metrics (N50, L50, GC%) |
| `ARG_abundance.csv` | Antibiotic resistance gene abundance (TPM) |
| `ARG_risk_scores.csv` | Complete ARG transfer risk assessment |
| `pathogen_abundance.csv` | WHO priority pathogen abundance |
| `phylum_composition.csv` | Phylum-level taxonomic composition |

### Supplementary Materials

Complete supplementary information including methods, tables, and figures is available:
- **Supplementary Document**: `docs/supplementary.md`
- **Full Data Tables**: Available upon request or in journal supplementary materials

---

## 📖 Citation

If you use this code or data, please cite:

```bibtex
@article{khan2026hospital,
  title={Hospital-level antimicrobial resistance in metagenomic wastewater surveillance},
  author={Khan, Ishaq and Naeem, Ihtisham and Ali, Shujait and Gulbin, Mahnoor and Iqbal, Arshad and Shafiq, Muhammad},
  journal={[Journal Name]},
  year={2026},
  doi={[DOI]}
}
```

**Code Repository**:
```bibtex
@software{khan2026code,
  author={Khan, Ishaq and Naeem, Ihtisham},
  title={Code for: Hospital-level antimicrobial resistance in metagenomic wastewater surveillance},
  year={2026},
  url={https://github.com/yourusername/mardan-wastewater-amr},
  doi={10.5281/zenodo.XXXXXX}
}
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues or pull requests.

### Reporting Issues

If you encounter any problems or have questions:
1. Check existing [issues](https://github.com/yourusername/mardan-wastewater-amr/issues)
2. Create a new issue with detailed description
3. Include error messages and system information

---

## 👥 Contact

**Principal Investigator**:  
Ishaq Khan, PhD 
Center for Biotechnology & Microbiology  
University of Swat, Pakistan  
📧 ishaq@uswat.edu.pk

**student researcher**
Ihtisham Naeem
Center for Biotechnology & Microbiology  
University of Swat, Pakistan  
ihtishamnaeem36@gmail.com



**For technical questions about the code**:  
Please open an issue on GitHub 

---

##  Acknowledgments

- Funding: This study was supported by the National Natural Science Foundation of China for International Young Scientists (Grant No. 42150410383) and the SUMC Scientific Research Initiation Grant (SRIG) (Grant No. 009-510858073).
- BioinCloud platform for metagenomic analysis
- NCBI, CARD, SILVA, and rrnDB databases
- WHO Priority Pathogens List 2024

---

## 🔗 Related Resources

- [WHO Priority Pathogens List 2024](https://www.who.int/news/item/...)
- [CARD Database](https://card.mcmaster.ca/)
- [BioinCloud Platform](https://www.bioincloud.tech/)
- [SILVA Database](https://www.arb-silva.de/)

---

**Last Updated**: May 11, 2026. 
**Version**: 1.0.0

---

## ⚠️ Important Notes

1. **Computational Requirements**:
   - RAM: Minimum 16 GB (32 GB recommended)
   - Storage: ~50 GB for complete pipeline
   - Processing time: ~2-4 hours for complete analysis

2. **Data Privacy**:
   - No personal or identifiable information included
   - Environmental samples only
   - Compliant with institutional ethics approval

3. **Reproducibility**:
   - All random seeds are set for reproducibility
   - Software versions specified in `environment.yml` and in supplementary file 
   - Analysis timestamps included in outputs

---

<div align="center">

**⭐ If you find this work useful, please star the repository! ⭐**

</div>
