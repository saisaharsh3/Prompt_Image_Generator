# 🎨 Prompt Image Generator

An advanced **Text-to-Image AI** web application that generates **photorealistic** images from user prompts using **Stable Diffusion**. Designed for **artists, designers, and AI enthusiasts**, this project leverages **PyTorch, Diffusers, and Flask** for an efficient and seamless experience.

---

## 🌟 Features

✅ **High-Quality Image Generation** – Uses **Realistic Vision V5.1**, a fine-tuned version of Stable Diffusion, for detailed and sharp images.  
✅ **Fast Inference with Optimizations** – Supports **CUDA acceleration** and **attention slicing** for smooth performance.  
✅ **User-Friendly Web Interface** – Clean and responsive **HTML, CSS, and JavaScript** frontend.  
✅ **Advanced Prompt Processing** – Enhances prompts to improve **realism, sharpness, and lighting**.  
✅ **Negative Prompt Filtering** – Removes unwanted styles (e.g., anime, cartoons, blurry images).  
✅ **Lightweight and Efficient** – Designed for both **local and cloud-based deployments**.  

---

## 🛠️ Tech Stack

| Component  | Technology Used |
|------------|----------------|
| **Backend** | Flask, Python, PyTorch, Diffusers |
| **Frontend** | HTML, CSS, JavaScript |
| **AI Model** | Stable Diffusion - Realistic Vision V5.1 |
| **Deployment** | Works locally on CPU/GPU, cloud deployment possible |
| **Dependencies** | `torch`, `flask`, `diffusers`, `flask_cors`, `Pillow` |

---

## 🚀 Installation Guide

### 📌 Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **pip (Python Package Manager)**
- **CUDA-compatible GPU** (for faster processing, optional)

### 🔧 Setup Instructions

1️⃣ Access the Web App

Open your browser and go to:
http://127.0.0.1:5000/


🎨 How to Use
Enter a Text Prompt
Example: "A futuristic city at sunset, ultra-detailed, 4K"
Click Generate
The AI will process your prompt and generate an image.
View & Download the Image
The generated image will be displayed on the page.
Refine & Experiment
Modify prompts for different results!


🏞️ Example Prompts & Outputs
Prompt	Sample Image
"A hyperrealistic lion in the wild, cinematic lighting"	🦁
"A cozy cabin in the snowy mountains, warm lights, ultra-detailed"	🏡
"A futuristic cyberpunk city at night, neon lights, 4K"	🌆
Try different combinations of styles, settings, and lighting for unique results!


⚡ Optimization Features
✅ CUDA Support – Uses GPU acceleration for faster image generation.
✅ Efficient Memory Management – Uses attention slicing & sequential CPU offloading.
✅ Negative Prompting – Filters out unwanted styles like cartoon, blurry, distorted images.
🌍 Future Enhancements
🔹 Cloud Deployment – Deploy to AWS/GCP/Azure for online usage.
🔹 Multiple Model Support – Switch between different Stable Diffusion models.
🔹 Image Upscaling – Implement Super Resolution AI for sharper outputs.
🔹 Batch Image Generation – Generate multiple images in one request.

📧 Contact & Support
👨‍💻 Author: Sai Saharsh Chittimilla
📌 GitHub: saisaharsh3
✉️ Email: saisaharsh3@gmail.com