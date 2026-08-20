from moviepy import ImageClip, concatenate_videoclips

scenes = [
    "scene1.png",
    "scene2.png",
    "scene3.png",
    "scene4.png",
    "ending.png"
]

clips = []

for scene in scenes:
    path = "generated/scenes/" + scene

    print(f"Processing {scene}...", flush=True)

    clip = ImageClip(path).with_duration(4)

    # Slow zoom effect
    clip = clip.resized(lambda t: 1 + 0.02 * t)

    clips.append(clip)

video = concatenate_videoclips(
    clips,
    method="compose"
)

print("Starting video encoding...", flush=True)

video.write_videofile(
    "generated/scenes/episode1.mp4",
    fps=20,
    codec="libx264",
    audio=False,
    preset="ultrafast",
    logger="bar"
)

video.close()

print("Episode 1 animated video created!", flush=True)