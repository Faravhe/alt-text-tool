from flask import Flask,request, jsonify
from mlx_vlm import load, apply_chat_template, generate
from PIL import Image
import tempfile
import os

app = Flask(__name__)

MODEL_PATH = "mlx-community/Qwen2-VL-7B-Instruct-4bit"      

print("Loading model, this happens once at startup...")
model, processor = load(MODEL_PATH)
config = model.config
print("Model loaded and ready.")

PROMPTS = {
	"simple": "Describe this image in one plain, simple sentence for use as alt-text. Use everyday words everyone can understand.",
	"creative": "Describe this image in one or two vivid, evocative sentences, as if it were a line from a science fiction story or a poem. Still describe only what is actually in the image.",
}

def preprocess_image(path, max_size=1024):
	img = Image.open(path)
	img = img.convert("RGB")
	img.thumbnail((max_size, max_size))
	processed_path = path.replace(".jpg", "_processed.jpg")
	img.save(processed_path, "JPEG")
	return processed_path

def run_prompt(image_path, prompt_text):
	prompt = apply_chat_template(processor, config, prompt_text, num_images=1)
	result = generate(model, processor, prompt, [image_path], verbose=False)
	return result.text.strip()

@app.route("/describe", methods=["POST"])
def describe():
	if "image" not in request.files:
		return jsonify({"error": "No image provided"}), 400

	image_file = request.files["image"]

	with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
		image_file.save(tmp.name)
		tmp_path = tmp.name

	processed_path = preprocess_image(tmp_path)

	try:
		simple_text = run_prompt(processed_path, PROMPTS["simple"])
		creative_text = run_prompt(processed_path, PROMPTS["creative"])
	finally:
		os.remove(tmp_path)
		os.remove(processed_path)

	return jsonify({
		"alt_text_simple": simple_text,
		"alt_text_creative": creative_text,
	})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=6000, debug=False)
