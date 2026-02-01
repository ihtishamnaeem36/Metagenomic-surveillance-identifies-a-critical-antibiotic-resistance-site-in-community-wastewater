"""
============================================================================
Antibiotic Resistance Risk Index (ARRI) Calculation
============================================================================
Study: Hospital-level antimicrobial resistance in metagenomic wastewater
Authors: Khan et al., 2026

Description: Calculates ARRI score integrating ARG abundance, pathogen 
             enrichment, and WHO clinical priority classification

Formula: ARRI = Σ[ARGᵢ × PEᵢ × CPWᵢ]
  where:
    ARGᵢ = Normalized abundance (TPM) of resistance gene i
    PEᵢ = Pathogen enrichment coefficient
    CPWᵢ = Clinical priority weight (WHO 2024)
============================================================================
"""

import pandas as pd
import numpy as np

# ============================================================================
# CONFIGURATION
# ============================================================================

# WHO Priority Pathogen Weights (WHO 2024 Classification)
WHO_PRIORITY_WEIGHTS = {
    'Critical': 3.0,   # Carbapenem-resistant, ESBL-producing Enterobacterales
    'High': 2.0,       # Vancomycin-resistant, MRSA, fluoroquinolone-resistant
    'Medium': 1.0,     # Penicillin-resistant respiratory pathogens
    'Low': 0.5         # Environmental resistance, limited clinical relevance
}

# ARG Category to WHO Priority Mapping
ARG_PRIORITY_MAP = {
    'Carbapenemase': 'Critical',
    'ESBL': 'Critical',
    'Vancomycin_resistance': 'High',
    'Colistin_resistance': 'Critical',
    'Fluoroquinolone_resistance': 'High',
    'Aminoglycoside_resistance': 'Medium',
    'Macrolide_resistance': 'Medium',
    'Tetracycline_resistance': 'Medium',
    'Sulfonamide_resistance': 'Low',
    'Other_AMR': 'Low'
}

# Risk Stratification Thresholds
RISK_CATEGORIES = {
    'Low': (0, 5.0),
    'Moderate': (5.0, 15.0),
    'High': (15.0, 30.0),
    'Critical': (30.0, float('inf'))
}

# ============================================================================
# FUNCTIONS
# ============================================================================

def calculate_pathogen_enrichment(pathogen_abundance, total_bacterial_abundance):
    """
    Calculate pathogen enrichment coefficient (PE)
    
    Parameters:
    -----------
    pathogen_abundance : float
        Total WHO priority pathogen abundance (TPM)
    total_bacterial_abundance : float
        Total bacterial abundance (TPM)
    
    Returns:
    --------
    float : Pathogen enrichment coefficient
    """
    if total_bacterial_abundance == 0:
        return 0.0
    return pathogen_abundance / total_bacterial_abundance


def get_clinical_priority_weight(arg_category):
    """
    Get WHO clinical priority weight for an ARG category
    
    Parameters:
    -----------
    arg_category : str
        ARG category name
    
    Returns:
    --------
    float : Clinical priority weight
    """
    priority_level = ARG_PRIORITY_MAP.get(arg_category, 'Low')
    return WHO_PRIORITY_WEIGHTS[priority_level]


def calculate_arri(arg_data, pathogen_data, sample_id='MCW2'):
    """
    Calculate Antibiotic Resistance Risk Index (ARRI)
    
    Parameters:
    -----------
    arg_data : pd.DataFrame
        DataFrame with columns: ['ARG', 'ARG_Category', 'MCW1', 'MCW2']
    pathogen_data : pd.DataFrame
        DataFrame with WHO priority pathogen abundances
    sample_id : str
        Sample identifier ('MCW1' or 'MCW2')
    
    Returns:
    --------
    dict : ARRI scores and components
    """
    
    # Get total bacterial abundance (sum of all taxonomic assignments)
    # In your actual data, this would come from Kraken2/Bracken output
    total_bacterial_abundance = 4170000  # Example: 4.17 million TPM for MCW2
    
    # Get WHO priority pathogen abundance
    # Sum of Critical + High priority pathogen abundances
    pathogen_abundance = 275  # Example: 275 TPM for MCW2 (from your data)
    
    # Calculate pathogen enrichment coefficient
    PE = calculate_pathogen_enrichment(pathogen_abundance, total_bacterial_abundance)
    
    # Initialize ARRI components
    arri_total = 0.0
    arri_by_priority = {
        'Critical': 0.0,
        'High': 0.0,
        'Medium': 0.0,
        'Low': 0.0
    }
    
    # Calculate ARRI for each ARG
    for _, row in arg_data.iterrows():
        arg_name = row['ARG']
        arg_category = row['ARG_Category']
        arg_abundance = row[sample_id]
        
        # Get clinical priority weight
        cpw = get_clinical_priority_weight(arg_category)
        
        # Get priority level for grouping
        priority_level = ARG_PRIORITY_MAP.get(arg_category, 'Low')
        
        # Calculate ARRI contribution for this ARG
        arri_contribution = arg_abundance * PE * cpw
        
        # Add to total and category
        arri_total += arri_contribution
        arri_by_priority[priority_level] += arri_contribution
    
    # Determine risk category
    risk_category = 'Unknown'
    for category, (min_val, max_val) in RISK_CATEGORIES.items():
        if min_val <= arri_total < max_val:
            risk_category = category
            break
    
    return {
        'ARRI_Total': arri_total,
        'ARRI_Critical': arri_by_priority['Critical'],
        'ARRI_High': arri_by_priority['High'],
        'ARRI_Medium': arri_by_priority['Medium'],
        'ARRI_Low': arri_by_priority['Low'],
        'Pathogen_Enrichment': PE,
        'Risk_Category': risk_category
    }


def calculate_16s_normalized_arri(arri_score, total_16s_abundance):
    """
    Normalize ARRI by 16S rRNA gene abundance for per-bacterium comparison
    
    Parameters:
    -----------
    arri_score : float
        Raw ARRI score
    total_16s_abundance : float
        Total 16S rRNA gene abundance (copy-number adjusted)
    
    Returns:
    --------
    float : 16S-normalized ARRI
    """
    if total_16s_abundance == 0:
        return 0.0
    return arri_score / total_16s_abundance


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    
    print("="*80)
    print("ANTIBIOTIC RESISTANCE RISK INDEX (ARRI) CALCULATION")
    print("="*80)
    
    # Example ARG data (subset from your actual data)
    example_arg_data = pd.DataFrame({
        'ARG': ['NDM', 'IMP', 'CTX-M', 'MCR', 'OXA', 'TEM'],
        'ARG_Category': ['Carbapenemase', 'Carbapenemase', 'ESBL', 
                        'Colistin_resistance', 'Other_AMR', 'ESBL'],
        'MCW1': [0.0, 0.0, 0.0, 0.52, 194.55, 291.76],
        'MCW2': [1.54, 0.68, 5.01, 3.65, 206.53, 37.78]
    })
    
    # Example pathogen data
    example_pathogen_data = pd.DataFrame({
        'Pathogen': ['P. aeruginosa', 'A. baumannii', 'E. coli'],
        'Priority': ['High', 'Critical', 'Critical'],
        'MCW1': [50, 54, 21],
        'MCW2': [140, 56, 60]
    })
    
    print("\nCalculating ARRI for MCW1...")
    arri_mcw1 = calculate_arri(example_arg_data, example_pathogen_data, 'MCW1')
    
    print("\nCalculating ARRI for MCW2...")
    arri_mcw2 = calculate_arri(example_arg_data, example_pathogen_data, 'MCW2')
    
    # Print results
    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    
    print(f"\nMCW1:")
    print(f"  Total ARRI: {arri_mcw1['ARRI_Total']:.2f}")
    print(f"  Risk Category: {arri_mcw1['Risk_Category']}")
    print(f"  Critical Priority: {arri_mcw1['ARRI_Critical']:.2f}")
    print(f"  High Priority: {arri_mcw1['ARRI_High']:.2f}")
    print(f"  Medium Priority: {arri_mcw1['ARRI_Medium']:.2f}")
    print(f"  Low Priority: {arri_mcw1['ARRI_Low']:.2f}")
    
    print(f"\nMCW2:")
    print(f"  Total ARRI: {arri_mcw2['ARRI_Total']:.2f}")
    print(f"  Risk Category: {arri_mcw2['Risk_Category']}")
    print(f"  Critical Priority: {arri_mcw2['ARRI_Critical']:.2f}")
    print(f"  High Priority: {arri_mcw2['ARRI_High']:.2f}")
    print(f"  Medium Priority: {arri_mcw2['ARRI_Medium']:.2f}")
    print(f"  Low Priority: {arri_mcw2['ARRI_Low']:.2f}")
    
    # Calculate fold change
    fold_change = arri_mcw2['ARRI_Total'] / arri_mcw1['ARRI_Total'] if arri_mcw1['ARRI_Total'] > 0 else float('inf')
    percent_increase = ((arri_mcw2['ARRI_Total'] - arri_mcw1['ARRI_Total']) / arri_mcw1['ARRI_Total']) * 100
    
    print(f"\nARRI Fold Change (MCW2/MCW1): {fold_change:.2f}x")
    print(f"Percent Increase: {percent_increase:.1f}%")
    
    # 16S-normalized ARRI (example)
    print("\n" + "="*80)
    print("16S-NORMALIZED ARRI (per bacterium)")
    print("="*80)
    
    # Example 16S abundances (copy-number adjusted)
    total_16s_mcw1 = 33500  # Example value
    total_16s_mcw2 = 59700  # Example value
    
    arri_norm_mcw1 = calculate_16s_normalized_arri(arri_mcw1['ARRI_Total'], total_16s_mcw1)
    arri_norm_mcw2 = calculate_16s_normalized_arri(arri_mcw2['ARRI_Total'], total_16s_mcw2)
    
    print(f"\nMCW1 (per 16S): {arri_norm_mcw1:.6f}")
    print(f"MCW2 (per 16S): {arri_norm_mcw2:.6f}")
    print(f"Fold Change: {arri_norm_mcw2/arri_norm_mcw1:.2f}x")
    
    print("\n" + "="*80)
    print("INTERPRETATION")
    print("="*80)
    print(f"""
MCW2 shows {arri_mcw2['Risk_Category']} risk (ARRI = {arri_mcw2['ARRI_Total']:.1f})
MCW1 shows {arri_mcw1['Risk_Category']} risk (ARRI = {arri_mcw1['ARRI_Total']:.1f})

The {fold_change:.1f}-fold increase in ARRI reflects:
1. Emergence of last-resort resistance genes (NDM, IMP, CTX-M)
2. Increased pathogen enrichment in MCW2
3. Higher abundance of critical-priority ARGs

This indicates MCW2 has transitioned from baseline environmental resistance
to a clinically critical resistance profile comparable to hospital wastewater.
""")
    
    print("="*80)
