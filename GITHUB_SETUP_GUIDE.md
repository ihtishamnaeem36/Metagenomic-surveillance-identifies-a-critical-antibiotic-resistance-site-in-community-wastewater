#  QUICK START GUIDE: Setting Up Your GitHub Repository

## Step-by-Step Instructions

### 1 Create GitHub Account (if needed)
- Go to https://github.com
- Sign up for free account
- Verify email address

---

### 2 Create New Repository

1. Click **"New"** button (green, top right)
2. **Repository name**: `mardan-wastewater-amr` (or your choice)
3. **Description**: 
   ```
   Code and analysis scripts for metagenomic surveillance of antimicrobial 
   resistance in community wastewater from Mardan District, Pakistan
   ```
4. **Public**  (Must be public for journal requirements)
5.  Add README file
6. Choose license: **MIT License**
7. Click **"Create repository"**

---

### 3 Upload Files to GitHub

#### Option A: Using GitHub Web Interface (Easiest)

1. In your new repository, click **"Add file"** → **"Upload files"**
2. Drag and drop these files:
   - `01_domain_composition.R`
   - `02_phylum_abundance.R`
   - `03_ARRI_calculation.py`
   - `README.md`
   - `environment.yml`
   - `requirements.txt`
   - `LICENSE`
3. Add commit message: "Initial commit: Add analysis scripts"
4. Click **"Commit changes"**

#### Option B: Using Git Command Line

```bash
# Initialize git in your local directory
cd /path/to/your/files
git init
git add .
git commit -m "Initial commit: Add analysis scripts"

# Link to GitHub repository
git remote add origin https://github.com/[yourusername]/mardan-wastewater-amr.git
git branch -M main
git push -u origin main
```

---

### 4️⃣ Create Release for Zenodo

1. In your GitHub repo, click **"Releases"** (right sidebar)
2. Click **"Create a new release"**
3. **Tag version**: `v1.0.0`
4. **Release title**: `Initial Release - Manuscript Submission v1.0.0`
5. **Description**:
   ```
   First release of analysis code accompanying the manuscript:
   "Hospital-level antimicrobial resistance in metagenomic wastewater surveillance"
   
   Includes:
   - Domain and phylum-level composition analysis (R)
   - ARRI calculation implementation (Python)
   - Complete documentation
   ```
6. Click **"Publish release"**

---

### 5 Get Zenodo DOI

1. Go to https://zenodo.org
2. Click **"Log in"** → Sign in with GitHub
3. Go to **Account** → **GitHub** 
4. Find your repository in the list
5. **Toggle ON** the repository
6. Go back to GitHub and create a release (if you haven't already)
7. Zenodo automatically creates DOI
8. **Copy the DOI** (e.g., `10.5281/zenodo.1234567`)

---

### 6️⃣ Add DOI Badge to README

1. Go to your Zenodo record
2. Copy the DOI badge markdown code
3. Edit your `README.md` on GitHub
4. Replace the placeholder badge with your actual DOI badge:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXX)
```

---

### 7️⃣ Create Folder Structure (Optional but Recommended)

Create these folders in your repository:

```
mardan-wastewater-amr/
├── scripts/          ← Move your code files here
├── data/             ← Add sample metadata (no raw FASTQ!)
├── results/          ← Add example outputs
│   ├── figures/
│   └── tables/
└── docs/             ← Additional documentation
```

**To create folders on GitHub web:**
1. Click "Add file" → "Create new file"
2. Type `scripts/.gitkeep` (this creates a folder)
3. Commit
4. Move files into folders by editing

---

### 8️⃣ Update Your Manuscript

#### In the Methods Section:
```
All bioinformatics analyses were performed using open-source software 
(Supplementary Table SX). Custom analysis scripts are available at 
https://github.com/[yourusername]/mardan-wastewater-amr.
```

#### Data Availability Section:
```
Data Availability

Raw sequencing data have been deposited in the NCBI Sequence Read Archive 
under BioProject accession PRJNA[XXXXXX]. Processed data are available in 
the Supplementary Materials. All code used for data analysis is freely 
available at https://github.com/[yourusername]/mardan-wastewater-amr and 
archived on Zenodo (DOI: 10.5281/zenodo.XXXXXX).
```

---

### 9️⃣ Final Checklist Before Submission

- [ ] GitHub repository is **PUBLIC**
- [ ] All code files uploaded
- [ ] README.md is complete with installation instructions
- [ ] LICENSE file included (MIT)
- [ ] Release created (v1.0.0)
- [ ] Zenodo DOI obtained
- [ ] DOI badge added to README
- [ ] Repository URL added to manuscript
- [ ] Tested that code runs on fresh environment

---

## 📋 What NOT to Upload to GitHub

❌ **DO NOT upload**:
- Raw FASTQ files (too large, use NCBI SRA instead)
- Large data files >100 MB
- Personal/private information
- Passwords or API keys
- Unpublished/proprietary data

✅ **DO upload**:
- Code scripts (.R, .py, .ipynb)
- Documentation (README, markdown files)
- Small data files (<10 MB)
- Example outputs
- Configuration files (environment.yml)

---

## 🆘 Troubleshooting

### Problem: Files too large for GitHub
**Solution**: Use Git LFS or upload to Zenodo separately

### Problem: Forgot to add LICENSE
**Solution**: Add it later via "Add file" → "Create new file" → name it `LICENSE`

### Problem: Need to update after submission
**Solution**: 
1. Make changes
2. Create new release (v1.0.1)
3. Update manuscript if needed (usually not required)

---

## 📧 Need Help?

- GitHub documentation: https://docs.github.com
- Zenodo help: https://help.zenodo.org
- Email me: ishaq@uswat.edu.pk

---

## ⏱️ Estimated Time

- Creating repository: **5 minutes**
- Uploading files: **10 minutes**
- Creating release: **5 minutes**
- Getting Zenodo DOI: **10 minutes**
- **Total: ~30 minutes**

---

## 🎯 Your Final GitHub URL

After setup, your repository will be at:
```
https://github.com/[yourusername]/mardan-wastewater-amr
```

**Use this URL in your manuscript's Data Availability statement!**

---

Good luck! 🚀
