# Masterclass: Multimodal Visual Language Models (VLM)

> [!IMPORTANT] Gist
> Multimodal models like **Gemma-3** integrate vision and language encoders, allowing the model to "see" an image and reason about it in natural language (e.g., Devanagari text extraction).

## 1. Vision-Language Integration
Modern VLMs (Vision-Language Models) typically use:
- **Vision Encoder**: A Vision Transformer (ViT) or similar to extract spatial features from an image.
- **Language Model**: A Decoder-only model (like Gemma) that receives visual tokens alongside text tokens.
- **Cross-Attention / Projection**: A bridge layer that aligns visual features with the text embedding space.

## 2. Practical Task: Devanagari OCR & Extraction
One of the most powerful applications for Nepali NLP is **Visual OCR**. Traditional OCR often struggles with complex ligatures in Devanagari, but VLMs use contextual reasoning to reconstruct the text.

### Workflow
1.  **Image Prep**: Loading the image (local path or URL).
2.  **Prompting**: Specifically instructing the model to output *only* Devanagari text to minimize hallucination.
3.  **Inference**: Using the `transformers` pipeline with the `image-text-to-text` task.

## 3. Comparative Advantages
| Feature | Traditional OCR (Tesseract) | VLM (Gemma-3) |
| :--- | :--- | :--- |
| **Ligature Handling** | Poor (requires manual rules) | Excellent (context-aware) |
| **Noise Tolerance** | Low (needs clean scans) | High (works with photos) |
| **Speed** | Fast | Slow (requires GPU) |
| **Customization** | Hard (requires retraining) | Easy (via prompting) |

---

**Notebook**: [vlm_inference_gemma.py](notebooks/vlm_inference_gemma.py) (Multimodal Devanagari Extraction)

#multimodal #vlm #gemma #ocr #nepali #devanagari #computer-vision
