const express = require("express");
const { execFile } = require("child_process");

const app = express();

const PORT = process.env.PORT || 3000;
const PYTHON = process.env.PYTHON || "python";

app.use(express.json());
app.use(express.static(__dirname));

app.post("/generate-video", (req, res) => {
    const { idea } = req.body;

    if (!idea) {
        return res.status(400).json({
            error: "Please enter a video idea"
        });
    }

    console.log("Generating scenes...");

    const sceneProcess = execFile(
        PYTHON,
        ["scenegenerator.py"],
        (sceneError, sceneOutput, sceneStderr) => {

            if (sceneError) {
                console.log("SCENE ERROR:");
                console.log(sceneStderr || sceneError);

                return res.status(500).json({
                    error: "Scene generation failed"
                });
            }

            console.log(sceneOutput);
            console.log("All scenes created successfully!");
            console.log("Creating animated video...");

            const videoProcess = execFile(
                PYTHON,
                ["make_video.py"]
            );

            videoProcess.stdout.on("data", (data) => {
                console.log("VIDEO:", data.toString());
            });

            videoProcess.stderr.on("data", (data) => {
                console.log("VIDEO ERROR:", data.toString());
            });

            videoProcess.on("error", (error) => {
                console.log("VIDEO PROCESS ERROR:");
                console.log(error);

                return res.status(500).json({
                    error: "Video process failed"
                });
            });

            videoProcess.on("close", (code) => {

                console.log("Video process exited with code:", code);

                if (code !== 0) {
                    return res.status(500).json({
                        error: "Video creation failed"
                    });
                }

                console.log("Video process completed!");
                console.log("Episode 1 animated video created!");

                return res.json({
                    success: true,
                    data: {
                        video: {
                            url: "/generated/scenes/episode1.mp4"
                        }
                    }
                });
            });
        }
    );
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`NovaStudio AI running on port ${PORT}`);
});