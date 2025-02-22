from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from diffusers import StableDiffusionPipeline, DDIMScheduler
import torch
from io import BytesIO

app = Flask(__name__)
CORS(app)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_id = "SG161222/Realistic_Vision_V5.1_noVAE"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  
    use_auth_token=False  
)


pipe = pipe.to(device)
pipe.enable_attention_slicing()  
pipe.enable_sequential_cpu_offload()  


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
        
        realistic_prompt = f"{prompt}, photorealistic, highly detailed, 4k quality, natural lighting, sharp focus"
        
    
        image = pipe(
            prompt=realistic_prompt,
            num_inference_steps=50,  
            guidance_scale=8.0,     
            height=448,             
            width=448,
            negative_prompt="cartoon, anime, painting, blurry, low quality, unrealistic, distorted"  
        ).images[0]

    
        img_io = BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": f"Error generating image: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)