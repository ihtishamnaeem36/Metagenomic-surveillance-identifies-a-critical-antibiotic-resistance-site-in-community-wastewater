# ============================================================================
# Domain-Level Microbial Community Composition Analysis
# ============================================================================
# Study: Hospital-level antimicrobial resistance in metagenomic wastewater
# Authors: Khan et al., 2026
# Description: Creates stacked bar plots showing relative abundance of 
#              Bacteria, Archaea, and Viruses/Phages in MCW1 and MCW2
# ============================================================================

# Load required packages
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
if (!requireNamespace("viridis", quietly = TRUE)) install.packages("viridis")

library(ggplot2)
library(viridis)

# ============================================================================
# INPUT DATA
# ============================================================================
# Domain-level composition percentages from Kraken2/Bracken classification

df <- data.frame(
  Sample     = c("MCW1", "MCW1", "MCW1", "MCW2", "MCW2", "MCW2"),
  Domain     = c("Bacteria", "Archaea", "Viral/Phage",
                 "Bacteria", "Archaea", "Viral/Phage"),
  Percentage = c(95.77, 3.68, 0.50,
                 99.28, 0.43, 0.22)
)

# ============================================================================
# CREATE VISUALIZATION
# ============================================================================

p <- ggplot(df, aes(x = Sample, y = Percentage, fill = Domain)) +
  geom_col(position = "stack", width = 0.6) +
  scale_fill_viridis_d(option = "viridis") +
  labs(
    title = "Domain-Level Microbial Community Composition\nin MCW1 and MCW2 Samples",
    x     = "Sample",
    y     = "Relative Abundance (%)"
  ) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title   = element_text(size = 13, hjust = 0.5, face = "bold"),
    axis.title   = element_text(size = 11),
    axis.text    = element_text(size = 10),
    legend.title = element_text(size = 10),
    legend.text  = element_text(size = 9),
    legend.position = "right"
  ) +
  ylim(0, 100)

# Display plot
print(p)

# ============================================================================
# SAVE OUTPUTS
# ============================================================================

# Save high-resolution PNG (300 dpi)
ggsave(
  filename = "domain_composition.png",
  plot     = p,
  width    = 6, height = 8, units = "in",
  dpi      = 300, bg = "white"
)

# Save vector PDF
ggsave(
  filename = "domain_composition.pdf",
  plot     = p,
  width    = 6, height = 8, units = "in",
  device   = cairo_pdf
)

cat("\nFiles saved:\n")
cat("  domain_composition.png (300 dpi)\n")
cat("  domain_composition.pdf (vector)\n")

# ============================================================================
# INTERPRETATION
# ============================================================================
# MCW1: 95.77% Bacteria, 3.68% Archaea, 0.50% Viral/Phage
# MCW2: 99.28% Bacteria, 0.43% Archaea, 0.22% Viral/Phage
#
# Key finding: MCW2 shows nearly complete bacterial dominance (99.3%) with
# dramatic reduction in archaeal abundance (3.7% → 0.4%), consistent with
# shift from anaerobic to aerobic conditions.
# ============================================================================
