from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from diffusers import StableDiffusionPipeline, DDIMScheduler
import torch
from io import BytesIO

app = Flask(__name__)
CORS(app)

# Device setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load Realistic Vision V5.1 (no VAE version for lower memory usage)
model_id = "SG161222/Realistic_Vision_V5.1_noVAE"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  # FP16 for low VRAM
    use_auth_token=False  # Set to True with your HF token if required
)

# Move to GPU and enable memory-efficient settings
pipe = pipe.to(device)
pipe.enable_attention_slicing()  # Reduce memory usage
pipe.enable_sequential_cpu_offload()  # Offload to CPU when VRAM is full

# Use DDIM scheduler for faster sampling
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Enhance prompt for realism
        realistic_prompt = f"{prompt}, photorealistic, highly detailed, 4k quality, natural lighting, sharp focus"
        
        # Generate image with realism-focused settings
        image = pipe(
            prompt=realistic_prompt,
            num_inference_steps=50,  # More steps for detail
            guidance_scale=8.0,     # Higher CFG for prompt fidelity
            height=448,             # Balanced resolution for 4GB VRAM
            width=448,
            negative_prompt="cartoon, anime, painting, blurry, low quality, unrealistic, distorted"  # Filter out unwanted styles
        ).images[0]

        # Save image to BytesIO
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": f"Error generating image: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)