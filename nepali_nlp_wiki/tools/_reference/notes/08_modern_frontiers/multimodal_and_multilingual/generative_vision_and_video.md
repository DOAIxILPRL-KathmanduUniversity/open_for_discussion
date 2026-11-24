# Generative Vision & Video

## 1. Vision Transformer (ViT)
ViT treats an image as a sequence of patches, applying the standard transformer encoder architecture to computer vision (Rothman, 2024).
1.  **Patching**: The image is split into fixed-size patches (e.g., $16 \times 16$).
2.  **Linear Projection**: Each patch is flattened and projected into an embedding space.
3.  **Positional Encoding**: Added to the patch embeddings to retain spatial information.
4.  **Transformer Encoder**: Processes the sequence of "image tokens" to learn global relationships.

## 2. CLIP (Contrastive Language-Image Pretraining)
CLIP bridges the gap between text and vision by learning a shared embedding space.
- **Dual Encoders**: Uses a text encoder and an image encoder (ViT or ResNet).
- **Contrastive Learning**: Trained to maximize the similarity between matching (Image, Text) pairs and minimize similarity for non-matching pairs.
- **Zero-shot Capability**: Can classify images into any category simply by providing a text description.

## 3. DALL-E 3 & Stable Diffusion
- **DALL-E 3**: Uses an LLM (GPT-4) to refine user prompts into highly descriptive instructions before generating the image via a diffusion model.
- **Stable Diffusion**: Utilizes a **U-Net** architecture with a transformer-based text encoder (CLIP) to guide the denoising process in latent space.
- **DAT (Divergent Association Task)**: Measuring the creativity of vision models by checking their ability to link semantically distant concepts.

## 4. Video Transformers
- **TimeSformer**: Extends the transformer to video by applying "divided space-time attention," analyzing patches across both spatial (within a frame) and temporal (between frames) dimensions.

> [!IMPORTANT] Gist
> Generative vision transcends the text-image boundary using Diffusion models, moving into the realm of automated ideation and video synthesis (Rothman, 2024).

## 1. Stable Diffusion
- **Text Embedding**: Using a transformer encoder to convert text prompts into vectors.
- **Noise & Latent Space**:
    1. Creating a random image with Gaussian noise.
    2. **Downsampling**: Reducing the image to a lower-dimensional latent space.
    3. **UNet & Attention**: Progressively "denoising" the latent image based on the text prompt.
    4. **Upsampling**: Reconstructing the final high-resolution image using a decoder.

## 2. Text-to-Video Synthesis
- **Frame-by-Frame Prediction**: Generating sequential images that maintain temporal consistency.
- **TimeSformer**: A vision transformer that captures space-time dependencies in videos (Video-to-Text).
- **Runway Gen-2**: Chaining models to animate static images or generate video from text descriptions.

## 3. DALL-E 3 & Creative Ideation
- **DALL-E 3**: Integrated with ChatGPT to refine user prompts automatically, enabling "Divergent Semantic Association" for highly creative imagery.

---

#modern-frontiers #generative-ai #stable-diffusion #text-to-video #dalle3
