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

    # প্ৰতিটো scene 5 second
    clip = ImageClip(path).with_duration(5)

    # ধীৰে ধীৰে zoom effect
    clip = clip.resized(lambda t: 1 + 0.03 * t)

    clips.append(clip)

video = concatenate_videoclips(
    clips,
    method="compose"
)

video.write_videofile(
    "generated/scenes/episode1.mp4",
    fps=24
)

print("Episode 1 animated video created!")