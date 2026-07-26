from mlx_vlm import load, apply_chat_template, generate 
model, processor = load('mlx-community/Qwen2-VL-7B-Instruct-4bit') 
config = model.config 
prompt = apply_chat_template(processor, config, 'Describe this image in one plain, simple sentence for use as alt-text.', num_images=1) 
result = generate(model, processor, prompt, ['test_images/img1_resized.jpg'], verbose=False) 
print(repr(result.text))  
