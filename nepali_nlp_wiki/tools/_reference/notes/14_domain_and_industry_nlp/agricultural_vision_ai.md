# Case Study: Krishi Chasma — Detecting Invasive Alien Plant Species

> [!IMPORTANT] Gist
> Krishi Chasma (Code No: AISP 322 / AISM 311), originally titled **"Semantic Video Retrieval in Nepali Language,"** is a specialized Software Development Kit (SDK) that integrates state-of-the-art Computer Vision for Nepal's agricultural monitoring. It targets edge deployment (Raspberry Pi/Mobile) for early detection and rapid response (EDRR).

## 1. Core Modules
The SDK is built on three pillars of deep learning:
- **Semantic Video/Image Search (CLIP)**: Utilizes Contrastive Language-Image Pretraining to retrieve visually similar images and video frames via vector encoding. This allows farmers to compare current crop health against a database using textual or image queries (e.g., "diseased tomato leaf").
- **Object Annotation/Detection (YOLOv7)**: Identifies and annotates specific issues like plant diseases, pests, and fruit counts for yield estimation.
- **Image Segmentation (U-Net)**: Isolates areas of interest, such as individual plants or diseased patches, to measure growth and track changes over time.

## 2. Dataset & Training
- **Volume**: 34,000 images covering 20 categories of IAPS (Invasive Alien Plant Species).
- **Architecture Comparisons**: 
    - **YOLOv11x**: 92% Top-1 Accuracy.
    - **DenseNet121**: 88% Accuracy.
    - **U-Net**: Evaluated using Intersection over Union (IoU) for segmentation precision.
- **Optimization**: Model conversion pipeline for **TensorFlow Lite (TFLite)** to enable on-device computation without cloud reliance (ideal for rural Nepal).

## 3. Implementation & SDK Features
- **Platform**: Python-based SDK using TensorFlow, PyTorch, and OpenCV.
- **Edge Support**: Raspberry Pi 4, Jetson Nano, and TFLite-compatible mobile devices.
- **AgriWiki Integration**: A Nepali language-based wiki providing real-time suggestions and disease information directly within the SDK environment.
- **Human-in-the-Loop**: Feedback mechanism for correcting incorrect detections to refine future models.

## 4. Key Species & Agricultural Focus
- **Species**: *Mikania micrantha* (लहरे बनमारा), *Lantana camara* (किर्ने काँडा), *Chromolaena odorata* (सेतो बनमारा).
- **Applications**: Pest identification, growth tracking, and harvest estimation (counting fruits/grains).

## 5. Technical Requirements
- **Hardware**: NVIDIA GPU (GTX 1050+) for training; 16GB RAM recommended.
- **Software**: Flask/FastAPI for API integration; Docker for containerization.

---

#applied-ai #computer-vision #nepali #agriculture #ecology #yolo #densenet #iaps
