# Masterclass: KrishiNet — Agricultural Survey Analysis

> [!IMPORTANT] Gist
> Real-world field data is often unstructured and inconsistent. Processing agricultural surveys involves meticulous data cleaning (sanitizing column names) and time-series analysis of soil health metrics.

## 1. Data Sanitization
Survey data from forms (e.g., Google Forms) often contains columns with spaces or leading/trailing whitespace (e.g., `"Field Code "`). 
- **The Fix**: Strip whitespace and replace spaces with underscores (`Field_Code`) using `.str.strip().str.replace(' ', '_')`. This prevents `ValueError` in visualization libraries like Seaborn.

## 2. Soil Health Analysis
Key metrics like **Soil pH** are analyzed to identify spatial and temporal trends.

### A. Temporal Distribution
Converting `Date` strings to `datetime` objects allows for sorting and plotting trends over time. 
- *Observation*: Identifying seasonal fluctuations in pH levels across different months.

### B. Spatial Variation (Field-wise)
Using **Box Plots** to compare pH distributions across different `Field_Code` entries.
- *Insight*: Identifying "outlier" fields with extreme acidity/alkalinity that require immediate intervention.

## 3. Integration with KrishiNet
This field data serves as the **Observation Layer** for the KrishiNet Knowledge Graph.
- **Node**: `Field_Code`
- **Attribute**: `soil_ph`
- **Relationship**: `HAS_OBSERVATION` (at a specific `Date`)

---

**Notebook**: [soil_health_analysis.py](notebooks/soil_health_analysis.py) (Survey Data Cleaning & Visualization)

#agriculture #krishinet #soil-health #data-cleaning #time-series #domain-nlp
