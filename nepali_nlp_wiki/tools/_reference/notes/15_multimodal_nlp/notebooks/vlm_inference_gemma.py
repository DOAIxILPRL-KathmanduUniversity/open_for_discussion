"""
🖼️ MULTIMODAL VLM INFERENCE (Gemma-3-4b-it)
-------------------------------------------
Extracts Devanagari text from images using Google's Gemma-3 VLM.
Demonstrates zero-shot visual reasoning and OCR.

Dependencies: pip install transformers accelerate torch pillow
"""

from transformers import pipeline
import torch

# --- CONFIGURATION ---
MODEL_ID = "google/gemma-3-4b-it"

def load_vlm_pipeline():
    print(f"Loading {MODEL_ID} (Multimodal)...")
    pipe = pipeline(
        "image-text-to-text", 
        model=MODEL_ID, 
        device_map="auto", 
        torch_dtype=torch.bfloat16
    )
    return pipe

def extract_devanagari(image_path, pipe):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image_path},
                {
                    "type": "text", 
                    "text": "What is written in this image in Devanagari? Output ONLY the exact Nepali/Devanagari text."
                }
            ]
        }
    ]
    print("Running inference...")
    output = pipe(text=messages)
    return output

if __name__ == "__main__":
    # pipe = load_vlm_pipeline()
    # result = extract_devanagari("path/to/nepali_signboard.jpg", pipe)
    # print(result)
    print("VLM Inference Module Ready.")
