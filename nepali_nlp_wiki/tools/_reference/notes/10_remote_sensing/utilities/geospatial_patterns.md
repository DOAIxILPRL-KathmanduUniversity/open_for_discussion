# Remote Sensing & Geospatial Utilities

This document distills the core ideas for handling satellite imagery and remote sensing data, extracted from the legacy `utils.py` and `generator.py` scripts.

## 1. Geospatial Image Patching
**Source**: `utils.py`

### The Idea
Satellite images (TIF/Raster) are often too large for GPU memory. Use a **Coordinate Patching Generator** to break images into manageable "chips" without losing spatial context.

### Logic Summary
- **Stride & Size**: Define a `patch_size` (e.g., 256x256) and a `stride` (e.g., 128 for overlap).
- **Coordinate Yielding**: Use a Python generator to yield $(x, y)$ start points across the `image_width` and `image_height`.
- **Data Preservation**: Ensure that all spectral bands (not just RGB) are preserved during patching.

---

## 2. Dataset Generation for Segmentation
**Source**: `generator.py` / `NepalDataset`

### The Idea
Standardize the **Image-Mask Alignment** for training deep learning models (like UNet or YOLOv8).

### Implementation Pattern
- **Basename Mapping**: Link images to masks using a naming convention (e.g., `area01.tif` -> `area01_mask.tif`).
- **Channel Normalization**: Automatically handle alpha-channel removal (dropping channel 4) and ensuring `uint8` conversion for display.
- **Tifffile Backend**: Use `tifffile` or `rasterio` instead of OpenCV for high-bitrate spectral data.

---

## 3. Evaluation of Spatial AI
**Source**: `Satellite Segmentation Nepal.ipynb`

### The Idea
Evaluate pixel-wise classification (segmentation) using **Intersection over Union (IoU)** or the **Dice Coefficient**, rather than simple pixel accuracy.
