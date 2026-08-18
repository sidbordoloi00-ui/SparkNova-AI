import torch
from diffusers import StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"

print("Loading AI model...")

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

prompt = """
A cute cartoon boy standing in a mysterious dark forest at night,
a magical glowing door between ancient trees,
cinematic lighting, high quality 3D animated movie style,
detailed environment, vertical composition,
no text, no letters, no watermark
"""

print("Generating image... This may take some time.")

image = pipe(
    prompt,
    num_inference_steps=20,
    guidance_scale=7.5,
    height=512,
    width=512
).images[0]

image.save("generated/scenes/test_ai_image.png")

print("AI image created successfully!")
print("Saved: generated/scenes/test_ai_image.png")