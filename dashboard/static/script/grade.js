      const photoInput = document.getElementById("photoInput");
    const photoContainer = document.getElementById("photoContainer");
    const uploadButton = document.getElementById("uploadButton");

    // Listen for file selection
    photoInput.addEventListener("change", () => {
        // Clear the photo container
        photoContainer.innerHTML = "";

        // Check if files are selected
        if (photoInput.files.length > 0) {
            console.log
            Array.from(photoInput.files).forEach((file) => {
                // Create an image preview for each selected file
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = document.createElement("img");
                    img.src = e.target.result;
                    photoContainer.appendChild(img);
                };
                reader.readAsDataURL(file);
            });

            // Enable the upload button
            uploadButton.disabled = false;
        } else {
            uploadButton.disabled = true;
        }
    });