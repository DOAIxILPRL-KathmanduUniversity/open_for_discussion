import easyocr
import cv2

# --- Initialize Reader ---
reader = easyocr.Reader(['en', 'ne'])

def perform_ocr(image_path):
    img = cv2.imread(image_path)
    if img is None: return "Error: Image not found."
    
    results = reader.readtext(img)
    for (bbox, text, prob) in results:
        print(f"Detected: {text} | Confidence: {prob:.2f}")
    return results

if __name__ == "__main__":
    # perform_ocr('certification.jpg')
    pass
