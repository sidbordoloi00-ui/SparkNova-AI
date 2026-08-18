const button = document.querySelector("#generateBtn");
const textarea = document.querySelector("#idea");
const styleSelect = document.querySelector("#style");
const status = document.querySelector("#status");

button.addEventListener("click", async () => {

    const idea = textarea.value.trim();

    if (!idea) {
        status.textContent = "Please enter video idea.";
        return;
    }

    button.disabled = true;
    button.textContent = "Generating...";

    status.textContent = "Creating scene...";

    try {

        const response = await fetch("/generate-video", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                idea: idea,
                style: styleSelect.value
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        status.innerHTML = `
            <h3>✅ Video Created</h3>

            <img 
            src="/generated/scenes/scene1.png"
            style="width:300px;border-radius:10px;margin:10px">

            <br>

            <video 
            controls
            src="${data.data.video.url}"
            style="width:300px;border-radius:10px">
            </video>
        `;


    } catch(error){

        status.textContent = "Error: " + error.message;

    } finally {

        button.disabled = false;
        button.textContent = "✨ Generate Video";

    }

});