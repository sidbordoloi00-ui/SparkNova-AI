const express = require("express");
const { execFile } = require("child_process");

const app = express();
const PORT = 3000;

const PYTHON = "C:\\Users\\Admin\\OneDrive\\AI-Video-Maker\\ai_env\\Scripts\\python.exe";

app.use(express.json());
app.use(express.static(__dirname));

app.post("/generate-video", (req, res) => {
    const { idea } = req.body;

    if (!idea) {
        return res.status(400).json({
            error: "Enter video idea"
        });
    }

    console.log("Generating scenes...");

    execFile(
        PYTHON,
        ["scenegenerator.py"],
        (sceneError, sceneOutput, sceneStderr) => {

            if (sceneError) {
                console.log(sceneStderr || sceneError);
                return res.status(500).json({
                    error: "Scene generation failed"
                });
            }

            console.log(sceneOutput);
            console.log("Creating animated video...");

            execFile(
                PYTHON,
                ["make_video.py"],
                (videoError, videoOutput, videoStderr) => {

                    if (videoError) {
                        console.log(videoStderr || videoError);
                        return res.status(500).json({
                            error: "Video creation failed"
                        });
                    }

                    console.log(videoOutput);

                    res.json({
                        success: true,
                        data: {
                            video: {
                                url: "/generated/scenes/episode1.mp4"
                            }
                        }
                    });
                }
            );
        }
    );
});

app.listen(PORT, "127.0.0.1", () => {
    console.log(`NovaStudio AI running at http://localhost:${PORT}`);
});