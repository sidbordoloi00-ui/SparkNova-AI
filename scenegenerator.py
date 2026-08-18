from PIL import Image, ImageDraw, ImageFont
import os

# Output folder
output_folder = "generated/scenes"
os.makedirs(output_folder, exist_ok=True)

# Image size - vertical Shorts format
width = 1080
height = 1920

# Scenes from Mystery Door Episode 1
scenes = [
    {
        "name": "scene1.png",
        "title": "Scene 1",
        "text": "A small boy walks alone\nin a quiet forest at night.\n\nSuddenly, he sees a\nmysterious glowing door\nbetween the trees."
    },
    {
        "name": "scene2.png",
        "title": "Scene 2",
        "text": "The boy slowly opens\nthe magical door.\n\nA beautiful hidden world\nappears behind it."
    },
    {
        "name": "scene3.png",
        "title": "Scene 3",
        "text": "The boy enters the new world.\n\nHe discovers strange glowing\nplants and magical creatures."
    },
    {
        "name": "scene4.png",
        "title": "Scene 4",
        "text": "A mysterious voice speaks...\n\nA BIG SECRET\nIS WAITING FOR YOU!"
    },
    {
        "name": "ending.png",
        "title": "THE MYSTERY DOOR",
        "text": "The door closes suddenly...\n\nTO BE CONTINUED..."
    }
]

# Different background colors for scenes
backgrounds = [
    (20, 35, 60),
    (45, 30, 80),
    (25, 70, 65),
    (60, 25, 70),
    (15, 15, 25)
]

# Load font
try:
    title_font = ImageFont.truetype("arial.ttf", 90)
    text_font = ImageFont.truetype("arial.ttf", 60)
except:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()


for i, scene in enumerate(scenes):

    # Create image
    image = Image.new(
        "RGB",
        (width, height),
        backgrounds[i]
    )

    draw = ImageDraw.Draw(image)

    # Draw title
    title = scene["title"]

    title_bbox = draw.textbbox(
        (0, 0),
        title,
        font=title_font
    )

    title_width = title_bbox[2] - title_bbox[0]

    draw.text(
        ((width - title_width) / 2, 250),
        title,
        font=title_font,
        fill="white"
    )

    # Draw story text
    text = scene["text"]

    bbox = draw.multiline_textbbox(
        (0, 0),
        text,
        font=text_font,
        align="center",
        spacing=25
    )

    text_width = bbox[2] - bbox[0]

    draw.multiline_text(
        ((width - text_width) / 2, 700),
        text,
        font=text_font,
        fill="white",
        align="center",
        spacing=25
    )

    # Save scene
    output_path = os.path.join(
        output_folder,
        scene["name"]
    )

    image.save(output_path)

    print("Created:", output_path)


print("\nAll scenes created successfully!")