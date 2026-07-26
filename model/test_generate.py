from mlx_vlm import load, apply_chat_template, generate
from PIL import Image
import os

MODEL_PATH = "mlx-community/Qwen2-VL-7B-Instruct-4bit"		#Qwens 7B model

print("Loading model...")
model, processor = load(MODEL_PATH)
config = model.config 
print("MODEL loaded.\n")

prompt_text = "Describe this image in one plain, simple sentence for use as alt-text."

images = ["test_images/img1.jpg", "test_images/img2.jpg", "test_images/img3.jpg"]

def preprocess_image(path, max_size=1024):
	img = Image.open(path)					#open the original image
	img = img.convert("RGB")				#normalized color mode
	img.thumbnail((max_size, max_size))			#resizes the img
	processed_path = path.replace(".jpg", "_processed.jpg")	
	img.save(processed_path, "JPEG")			#solve img's progresive issue
	return processed_path					#returns a new path file

for img in images:
	print(f"Describing {img}...")
	processed = preprocess_image(img)
	prompt = apply_chat_template(processor, config, prompt_text, num_images=1)
	result = generate(model, processor, prompt, [processed], verbose=False)
	print(f"{img} result:", result.text.strip())
	os.remove(processed)					#os.remove
	print()
