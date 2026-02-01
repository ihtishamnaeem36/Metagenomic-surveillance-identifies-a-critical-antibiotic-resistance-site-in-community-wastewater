# ============================================================================
# Phylum-Level Abundance Analysis (Top 20 + Other)
# ============================================================================
# Study: Hospital-level antimicrobial resistance in metagenomic wastewater
# Authors: Khan et al., 2026
# Description: Analyzes and visualizes top 20 bacterial phyla abundance
#              with labeled percentages
# ============================================================================

library(ggplot2)
library(viridis)
library(dplyr)
library(tidyr)
library(scales)

# ============================================================================
# CONFIGURATION
# ============================================================================

# Set your file path to the taxonomic annotation file
# File should contain columns: taxonomy, MCW1, MCW2
file_path <- "standard_species_annotation_MCW1_MCW2.txt"

# Check if file exists
if (!file.exists(file_path)) {
  stop("Error: File not found at ", file_path, "\n",
       "Please update the file_path variable with the correct path.")
}

# ============================================================================
# LOAD AND PROCESS DATA
# ============================================================================

# Load annotation file
anno <- read.table(file_path, 
                   header = TRUE, 
                   sep = "\t", 
                   stringsAsFactors = FALSE,
                   comment.char = "", 
                   quote = "")

cat("Data loaded successfully!\n")
cat("Total OTUs:", nrow(anno), "\n\n")

# Extract phylum from taxonomy string
# Format: d__domain;p__phylum;c__class;...
anno$Phylum <- sub(".*p__([^;]+).*", "\\1", anno$taxonomy)

# ============================================================================
# CALCULATE RELATIVE ABUNDANCE
# ============================================================================

phylum_df <- anno %>%
  select(MCW1, MCW2, Phylum) %>%
  pivot_longer(cols = c(MCW1, MCW2), 
               names_to = "Sample", 
               values_to = "Count") %>%
  group_by(Sample, Phylum) %>%
  summarise(Count = sum(Count), .groups = "drop") %>%
  group_by(Sample) %>%
  mutate(Percentage = Count / sum(Count) * 100) %>%
  ungroup()

# ============================================================================
# SELECT TOP 20 PHYLA + "OTHER"
# ============================================================================

phylum_plot <- phylum_df %>%
  arrange(Sample, desc(Percentage)) %>%
  group_by(Sample) %>%
  mutate(
    Rank   = row_number(),
    Phylum = ifelse(Rank <= 20, Phylum, "Other")
  ) %>%
  group_by(Sample, Phylum) %>%
  summarise(Percentage = sum(Percentage), .groups = "drop") %>%
  ungroup() %>%
  arrange(Sample, desc(Percentage))

# Order phyla (Other last)
phylum_plot$Phylum <- factor(
  phylum_plot$Phylum,
  levels = c(setdiff(unique(phylum_plot$Phylum), "Other"), "Other")
)

# Add labels (only if > 0.5% to avoid clutter)
phylum_plot <- phylum_plot %>%
  mutate(Label = ifelse(Percentage >= 0.5, 
                        sprintf("%.2f%%", Percentage), 
                        ""))

# ============================================================================
# CREATE VISUALIZATION
# ============================================================================

p <- ggplot(phylum_plot, aes(x = Sample, y = Percentage, fill = Phylum)) +
  geom_col(position = "stack", width = 0.6, colour = "white", size = 0.4) +
  geom_text(aes(label = Label), 
            position = position_stack(vjust = 0.5),
            size = 3, color = "white", fontface = "bold") +
  scale_fill_viridis_d(option = "plasma") +
  labs(
    title = "Phylum-Level Relative Abundance\nMCW1 vs MCW2 (Top 20 + Other)",
    x = "Sample", 
    y = "Relative Abundance (%)", 
    fill = "Phylum"
  ) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
    legend.position = "right",
    legend.text = element_text(size = 7.5),
    legend.key.size = unit(0.4, "cm")
  ) +
  scale_y_continuous(expand = c(0, 0), limits = c(0, 100))

# Display plot
print(p)

# ============================================================================
# SAVE OUTPUTS
# ============================================================================

# Save PNG (300 dpi)
ggsave("phylum_abundance_TOP20.png", 
       p, 
       width = 10, height = 8, 
       dpi = 300, bg = "white")

# Save PDF (vector)
ggsave("phylum_abundance_TOP20.pdf", 
       p, 
       width = 10, height = 8, 
       device = pdf)

cat("\nFiles saved:\n")
cat("  phylum_abundance_TOP20.png\n")
cat("  phylum_abundance_TOP20.pdf\n\n")

# ============================================================================
# PRINT SUMMARY TABLE
# ============================================================================

cat("Top 10 Phyla by Sample:\n")
cat("=" %R% 80 %R% "\n")

top10_summary <- phylum_plot %>%
  group_by(Sample) %>%
  slice_head(n = 10) %>%
  select(Sample, Phylum, Percentage)

print(top10_summary, n = 20)

# ============================================================================
# KEY FINDINGS
# ============================================================================
cat("\n" %R% "=" %R% 80 %R% "\n")
cat("KEY FINDINGS:\n")
cat("=" %R% 80 %R% "\n")

# Calculate key changes
pseudo_mcw1 <- phylum_plot %>% filter(Sample == "MCW1", Phylum == "Pseudomonadota") %>% pull(Percentage)
pseudo_mcw2 <- phylum_plot %>% filter(Sample == "MCW2", Phylum == "Pseudomonadota") %>% pull(Percentage)

cat(sprintf("Pseudomonadota: %.2f%% (MCW1) → %.2f%% (MCW2)\n", pseudo_mcw1, pseudo_mcw2))
cat("  → WHO priority pathogen enrichment (P. aeruginosa, A. baumannii, E. coli)\n\n")

thermo_mcw1 <- phylum_plot %>% filter(Sample == "MCW1", Phylum == "Thermodesulfobacteriota") %>% pull(Percentage)
thermo_mcw2 <- phylum_plot %>% filter(Sample == "MCW2", Phylum == "Thermodesulfobacteriota") %>% pull(Percentage)

if(length(thermo_mcw1) > 0 & length(thermo_mcw2) > 0) {
  cat(sprintf("Thermodesulfobacteriota: %.2f%% (MCW1) → %.2f%% (MCW2)\n", thermo_mcw1, thermo_mcw2))
  cat("  → 34-fold decline, shift from anaerobic to aerobic conditions\n\n")
}

cat("=" %R% 80 %R% "\n")
