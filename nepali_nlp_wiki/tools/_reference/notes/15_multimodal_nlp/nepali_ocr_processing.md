# Nepali OCR Processing (EasyOCR)

> [!IMPORTANT] Gist
> Optical Character Recognition (OCR) for Devanagari involves unique challenges such as the *Shirorekha* (headline) connecting characters. This module utilizes `EasyOCR` to perform multi-lingual (English/Nepali) text extraction from images.

## 1. Engine Configuration
We utilize the `EasyOCR` reader, which is based on the CRAFT text detector and a CRNN recognition model.
- **Languages**: `['en', 'ne']` - Simultaneous detection of English and Devanagari.
- **Backend**: PyTorch-based, supporting CUDA acceleration for industrial-grade batch processing.

## 2. Pre-processing & Visualization
To improve detection accuracy, images are often pre-processed using `OpenCV`:
- **Grayscaling**: Reducing noise.
- **Thresholding**: Enhancing character contrast against complex backgrounds (e.g., certifications, signage).
- **Bounding Boxes**: Visualizing text regions with confidence scores.

## 3. Post-processing Challenges
- **Segmentation**: Handling connected characters (Shirorekha).
- **Diacritics**: Ensuring *Matras* are correctly associated with their base consonants.
- **Dictionary Correction**: Post-OCR spell-checking using the `nepali-stemmer` or custom lexicons.

---

**Notebook**: [nepali_ocr_easyocr.py](notebooks/nepali_ocr_easyocr.py)

#multimodal #ocr #devanagari #opencv #easyocr #vision
