from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("generated/scenes", exist_ok=True)

W, H = 1080, 1920

def create_scene(filename, text, door=False, magic=False):
    img = Image.new("RGB", (W, H), (20, 30, 70))
    draw = ImageDraw.Draw(img)

    # forest background
    draw.rectangle((0, 700, W, H), fill=(30, 100, 50))

    for x in [100, 350, 800]:
        draw.rectangle((x, 500, x+50, 1100), fill=(90, 50, 20))
        draw.ellipse((x-120, 300, x+170, 700), fill=(20, 130, 60))

    # glowing door
    if door:
        draw.rectangle((380, 600, 700, 1200), fill=(100, 60, 30))
        draw.ellipse((470, 750, 610, 900), fill=(255, 230, 100))

    # magical world
    if magic:
        draw.ellipse((150, 400, 300, 550), fill=(100, 220, 255))
        draw.ellipse((750, 350, 900, 500), fill=(220, 120, 255))

    # boy
    draw.ellipse((470, 1200, 610, 1340), fill=(255, 200, 150))
    draw.rectangle((500, 1340, 580, 1600), fill=(40, 80, 200))

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = None

    draw.text((80, 1700), text, fill="white", font=font)

    img.save("generated/scenes/" + filename + ".png")


create_scene("scene1", "A boy finds a mysterious glowing door", True)
create_scene("scene2", "The magical door opens", True)
create_scene("scene3", "A hidden magical world appears", False, True)
create_scene("scene4", "A mysterious voice reveals a secret", False, True)
create_scene("ending", "The door closes... To be continued")

print("Episode 1 scenes created!")